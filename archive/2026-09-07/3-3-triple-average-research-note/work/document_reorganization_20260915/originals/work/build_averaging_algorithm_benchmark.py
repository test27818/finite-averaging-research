"""Package existing difficult instances and certificates without rerunning search."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from math import gcd
from pathlib import Path
import sys

sys.dont_write_bytecode = True

REPO = Path(__file__).resolve().parent.parent
OUT = Path('C:/Users/19226/Documents/Codex/2026-09-10/new-chat/outputs/averaging_algorithm_benchmark')


def read(name):
    return json.loads((REPO/'work'/name).read_text(encoding='utf-8'))


def write(name, data):
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def centered_g(values):
    n, total = len(values), sum(values)
    centered = [n*x-total for x in values]
    common = gcd(*centered)
    if not common:
        return None
    centered = [x//common for x in centered]
    return gcd(*(x-centered[0] for x in centered))


def relabel(source, destination, groups, base):
    positions = {}
    for i, value in enumerate(destination):
        positions.setdefault(value, []).append(i+1)
    mapping = [positions[value].pop() for value in source]
    assert all(not remaining for remaining in positions.values())
    return [[mapping[i-base] for i in group] for group in groups]


def steps_from_values(initial, p, moves):
    state, groups = list(map(F, initial)), []
    for move in moves:
        positions, indices = {}, []
        for i, value in enumerate(state):
            positions.setdefault(value, []).append(i)
        for value in move:
            indices.append(positions[F(value)].pop())
        assert len(indices) == len(set(indices)) == p
        mean = sum(state[i] for i in indices)/p
        for i in indices:
            state[i] = mean
        groups.append([i+1 for i in indices])
    assert not any(state)
    return groups


def main():
    OUT.mkdir(exist_ok=True)
    cases, metadata, refs, keys = [], {}, {}, {}
    seen_ids = set()
    historical = read('endpoint_reverse_candidate_paths.json')
    structured = read('endpoint_reverse_structured_inputs.json')
    escapes = read('endpoint_reverse_escape_certificates.json')
    source_aliases = {}

    def add(case_id, p, values, tags, details, expected=True):
        key = p, tuple(sorted(values))
        if key in keys:
            chosen = keys[key]
            metadata[chosen]['source_aliases'].append(case_id)
            source_aliases[case_id] = chosen
            return chosen
        assert case_id not in seen_ids
        seen_ids.add(case_id)
        cases.append({'id': case_id, 'p': p, 'n': len(values), 'input': list(map(str, values))})
        keys[key] = case_id
        source_aliases[case_id] = case_id
        metadata[case_id] = {'case_id': case_id, 'tags': tags,
            'expected_reachable': expected, 'G': centered_g(values),
            'max_abs_input_bits': max(abs(x).bit_length() for x in values),
            'reference_steps': None, 'source_aliases': [], 'details': details,
            'reachability_evidence': (
                'Project theorem in outputs/seven_average_fifteen_complete.md, read for scope; not reproved here.'
                if expected is True else
                'Known p<=n<=2p denominator obstruction and nonzero common mod2 residue.'
                if expected is False else
                'Extension input: G=1 checked; no complete endpoint theorem or path imported for this input.')}
        return case_id

    def save_reference(case_id, source_values, groups, index_base, origin):
        destination = list(map(int, next(x for x in cases if x['id'] == case_id)['input']))
        operations = relabel(source_values, destination, groups, index_base)
        if case_id not in refs or len(operations) < len(refs[case_id]['operations']):
            refs[case_id] = {'case_id': case_id, 'operations': operations,
                            'source': origin, 'optimality': 'reference upper bound; no general shortest claim'}
            metadata[case_id]['reference_steps'] = len(operations)
            metadata[case_id]['expected_reachable'] = True
            metadata[case_id]['reachability_evidence'] = 'Included original-position certificate independently verified.'

    small_ids = []
    for i, record in enumerate(escapes['certificates'], 1):
        case_id = add('frozen-small-%02d' % i, 7, record['input'],
            ['small_integer_frozen', 'fractions_required', 'no_zero_within_two_operations'],
            {'source': 'Complete canonical [-5,5] survey residual inputs',
             'nonconstant_integer_moves': 0, 'all_first_step_value_types_checked': True})
        small_ids.append(case_id)
        save_reference(case_id, record['input'], record['groups'], 0,
                       'endpoint_reverse_escape_certificates.json')

    for record in structured['records']:
        p, bound = record['p'], record['lift_bound']
        label = {'2': 'tiny', '64': 'small', '1000000': 'million',
                 '18446744073709551616': 'wide'}[bound]
        for i, candidate in enumerate(record['candidates'], 1):
            values = [candidate['background']]*candidate['frequency']+candidate['light']
            tags = ['structured_integer_frozen', 'fractions_required', 'scale_'+label]
            if candidate['three_step_zero_path'] is None:
                tags.append('no_two_disjoint_preparation_zero_certificate')
            case_id = add('frozen-p%d-%s-%03d' % (p, label, i), p, values, tags,
                {'generation': {'background': '1', 'frequency': candidate['frequency'],
                                'light': list(map(str, candidate['light'])), 'lift_bound': bound},
                 'historical_two_disjoint_preparation_test':
                    'outside_horizon' if candidate['three_step_zero_path'] is None else 'certified',
                 'nonconstant_integer_moves': 0}, expected=True if p == 7 else None)
            assert sum(values) == 0 and centered_g(values) == 1
            residue_total = sum((x-1) % p for x in candidate['light'])
            assert residue_total == p-1
            if candidate['three_step_zero_path'] is not None:
                save_reference(case_id, values, candidate['three_step_zero_path'], 0,
                               'endpoint_reverse_structured_inputs.json')

    chosen_ids, challenge_ids = [], []
    for result in historical['results']:
        case_id = keys[7, tuple(sorted(result['input']))]
        chosen_ids.append(case_id)
        meta = metadata[case_id]
        meta['historical_search'] = {
            'settings': historical['settings'], 'selection': result['selection'],
            **{k: result.get(k) for k in
               ('status', 'reason', 'steps', 'first_zero_depth', 'expanded', 'generated',
                'visited', 'solve_seconds', 'complete_search_depth')}}
        if result['status'] == 'solved':
            save_reference(case_id, result['input'], result['operations'], 1,
                           'endpoint_reverse_candidate_paths.json')
        else:
            challenge_ids.append(case_id)
            meta['tags'].append('historical_beam_depth24_no_path')

    # Method-regression example with a complete five-step certificate.
    values = [30]*23+[23]*23+[184]+[-15]*22+[-1073]
    protected_id = add('regression-protected-p23-n70', 23, values,
        ['method_regression', 'fixed_protection_failure'],
        {'purpose': 'Fixed protected position -1073 misses useful moves; dynamic role exchange succeeds.',
         'scope': 'The failure concerns a restricted selector, not every integer move.'})
    moves = [(184,)+(-15,)*6+(-1073,)+(30,)*15,
             (30,-15,-15)+(23,)*10+(-23,)*10,
             (30,)*7+(-15,)*14+(0,)*2,
             (23,)*11+(-23,)*11+(0,),
             (23,23,-23,-23)+(0,)*19]
    save_reference(protected_id, values, steps_from_values(values, 23, moves), 1,
                   'Uniform explicit five-step protected-exchange family')

    p = 7
    negative = add('control-negative-p7-n14', p, [-p]+[0]*(p-1)+[1]*p,
        ['negative_control'], {'purpose': 'A G=1 input that is truly unreachable at n=2p.'}, False)
    refs[negative] = {'case_id': negative, 'status': 'unreachable',
                     'source': 'Proved 2p denominator obstruction; not a search failure.'}
    positive_values = [-7]+[0]*7+[1]*7
    positive = add('control-zero-buffer-p7-n15', 7, positive_values,
        ['positive_control'], {'purpose': 'Adding one zero to the negative case permits four steps.'})
    tail = [(-7,)+(0,)*6, (-1,)*3+(1,)*3+(0,),
            (-1,)*3+(1,)*3+(0,), (-1,1)+(0,)*5]
    save_reference(positive, positive_values, steps_from_values(positive_values, 7, tail), 1,
                   'Explicit four-step zero-buffer family')
    constant = add('control-already-equal', 7, [4]*15, ['positive_control'],
                   {'purpose': 'Already equal, original target mean 4, zero operations.'})
    save_reference(constant, [4]*15, [], 1, 'Empty path for a constant input')

    case_by_id = {x['id']: x for x in cases}
    # Offline verification of every reference and input property.
    spec = importlib.util.spec_from_file_location('bench_verify', OUT/'verify_paths.py')
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    metrics = []
    for case_id, reference in refs.items():
        if reference.get('status') == 'unreachable':
            continue
        measured = verifier.verify_path(case_by_id[case_id], reference['operations'])
        metadata[case_id]['reference_metrics'] = measured
        metrics.append({'case_id': case_id, **measured})

    schema = {'schema_version': 1, 'index_base': 1, 'coordinate_encoding': 'exact integer strings'}
    write('cases.json', {**schema, 'cases': cases})
    write('p7_cases.json', {**schema, 'cases': [c for c in cases
          if c['p'] == 7 and c['n'] == 15 and c['id'].startswith('frozen-')]})
    write('scored_cases.json', {**schema, 'cases': [c for c in cases
          if metadata[c['id']]['expected_reachable'] is not None]})
    quick_ids = list(dict.fromkeys(small_ids+chosen_ids+[protected_id, negative, positive, constant]))
    write('quick_cases.json', {**schema, 'cases': [case_by_id[i] for i in quick_ids]})
    write('challenge_cases.json', {**schema, 'cases': [case_by_id[i] for i in challenge_ids]})
    write('reference_solutions.json', {'index_base': 1, 'solutions': list(refs.values())})
    write('reference_metrics.json', {'results': metrics})
    write('submission_template.json', {'solutions': [
        {'case_id': i, 'status': 'not_found'} for i in quick_ids]})

    sources = []
    for name in ('endpoint_reverse_structured_inputs.json', 'endpoint_reverse_candidate_paths.json',
                 'endpoint_reverse_escape_certificates.json'):
        sources.append({'file': name, 'sha256': sha256((REPO/'work'/name).read_bytes()).hexdigest()})
    summary = {'total_unique_cases': len(cases), 'endpoint_frozen_unique_cases': len(cases)-4,
               'original_structured_draws': 576, 'deduplicated_structured_cases':
                   len({(r['p'], tuple(sorted([1]*x['frequency']+x['light'])))
                        for r in structured['records'] for x in r['candidates']}),
               'quick_cases': len(quick_ids), 'challenge_cases': len(challenge_ids),
               'included_verified_solution_paths': len(metrics), 'known_negative_controls': 1,
               'cases_without_included_path': sum(
                   i not in refs for i in case_by_id),
               'main_p7_endpoint_cases': sum(c['p'] == 7 and c['n'] == 15
                   and c['id'].startswith('frozen-') for c in cases),
               'known_positive_cases': sum(m['expected_reachable'] is True for m in metadata.values()),
               'extension_cases_without_ground_truth': sum(m['expected_reachable'] is None
                                                          for m in metadata.values())}
    manifest = {'schema_version': 1, 'name': 'p-average difficult construction benchmark',
        'created': '2026-09-12', 'summary': summary,
        'problem': 'Replace exactly p distinct original positions by their arithmetic mean; '
                   'construct a finite path to the original global mean. No new positions.',
        'user_update': 'The user reports the question has been proved elsewhere. The project now contains '
                       'seven_average_fifteen_complete.md, which proves p7,n15. Preserve algorithmic difficulty.',
        'proof_scope': 'The p7,n15 theorem scope was read, not independently re-audited. Its G1 inputs are '
                       'positive. Other p19,p37 inputs are positive only when an explicit verified path is '
                       'included; remaining extension inputs have null expected_reachable.',
        'theorem_source': {'file': 'outputs/seven_average_fifteen_complete.md',
                          'sha256': sha256((REPO/'outputs/seven_average_fifteen_complete.md').read_bytes()).hexdigest()},
        'index_base': 1, 'integer_precision': 'Coordinates are strings, including values beyond 2**53.',
        'source_files': sources, 'source_aliases': source_aliases,
        'historical_sample_rows': [{k: v for k, v in r.items() if k != 'candidates'}
                                   for r in structured['records']],
        'case_metadata': list(metadata.values())}
    write('manifest.json', manifest)

    def compact(case):
        values = list(map(int, case['input']))
        return ', '.join('%s × %d' % (v, count) if count > 1 else str(v)
                         for v, count in Counter(values).items())

    lines = [
        '# p 平均算法能力测试集',
        '',
        '日期：2026-09-12。用途是测试具体路径构造能力。项目新文档已证明七平均十五元的 G=1 判据；本包将这组题全部作为已知可达的构造题。',
        '',
        '本包保留这次实际遇到的困难题面、旧算法预算和已知路径，不重新运行或提高搜索预算。七平均十五元未附路径的题仍是已知可达的构造任务；p=19、37 的扩展题若未附证书，则不设置可达性真值。已附路径另外经过独立精确验解。',
        '',
        '## 文件',
        '',
        '| 文件 | 用途 |',
        '|---|---|',
        '| cases.json | 全部 %d 道去重题面，只含 ID、p、n 和原始整数数组 |' % len(cases),
        '| p7_cases.json | %d 道已知可达、无整数出边的七平均十五元主测试题 |' % summary['main_p7_endpoint_cases'],
        '| scored_cases.json | %d 道可直接计正确率的题：已知正例与严格阴性对照 |' %
            (summary['known_positive_cases']+1),
        '| quick_cases.json | %d 道精选题，含小整数冻结态、逐级大数、历史未出解题及对照 |' % len(quick_ids),
        '| challenge_cases.json | 2 道旧束搜索深度 24 未构造出路径的大数题 |',
        '| manifest.json | 每题难点、证据来源、旧预算、重复别名与参考指标 |',
        '| reference_solutions.json | %d 条完整原位置路径和 1 个严格阴性对照答案；解题前可不提供 |' % len(metrics),
        '| verify_paths.py | 独立精确验解器，只有 Python 标准库依赖 |',
        '| generate_cases.py | 同结构新题生成器，用于避免只记忆现有题面 |',
        '| submission_template.json | 精选题输出模板，not_found 可替换为 operations |',
        '',
        '## 困难局面的分类',
        '',
        '1. **完全没有非恒等整数出边。** 7 道高度 5 的七平均十五元输入，以及生成集中的全部题，必须允许分数中间值。只在整数状态图搜索会直接停住。七个小例已有至多八步完整路径，不代表它们数学上难解或八步最短。',
        '2. **短预处理不够。** 576 次结构抽样中，481 次未命中“两次不交 p 块平均后出现零和 p 子集”的证书。题面按实际值去重为 574 道。这是一个具体机制和预算的排除，不能把它当成任意有理路径的不可达证明。',
        '3. **大整数与深度瓶颈。** 旧算法在数值提升至 10^6 的精选题找到 14、16 步路径；两道提升范围为 2^64 的精选题在深度 24 停止。这里的 2^64 是生成参数上界，实际坐标还乘了 p 并作总和补偿，可超过 64 位。',
        '4. **辅助记录使算法误判。** 二十三平均七十元的固定保护位置例子已有五步解，用来检查算法是否允许重选保护位置。另加 2p 的真正不可达对照，避免把所有 G=1 都当成可达。',
        '',
        '## 15 道核心题的参考表现',
        '',
        '| ID | p,n | 已保存路径步数 | 历史记录 |',
        '|---|---|---:|---|',
    ]
    for i in small_ids+chosen_ids:
        m, case = metadata[i], case_by_id[i]
        baseline = m.get('historical_search')
        status = '无整数出边；全部首步均不能造零和七元组'
        if baseline:
            status = ('束搜索找到证书，首次零坐标第 %s 步' % baseline['first_zero_depth']
                      if baseline['status'] == 'solved'
                      else '束宽 96，深度 24 到上限；未生成证书')
        lines.append('| %s | %d,%d | %s | %s |' %
                     (i, case['p'], case['n'], m['reference_steps'] or '待构造', status))
    lines += ['', '## 两道优先保留的大整数题', '']
    for i in challenge_ids:
        case = case_by_id[i]
        lines += ['**%s**：p=%d，n=%d，十份 1 加下面五个整数：' % (i, case['p'], case['n']), '',
                  '~~~text', '\n'.join(case['input'][-5:]), '~~~', '']
    lines += [
        '这两题全部满足总和为零、本原、G=1，且没有非恒等整数 p 平均。旧搜索配置是宽度 96、最多 24 层、3000 个展开节点、每题 8 秒预算，四进程执行；实际两题分别只展开 2136、2142 个节点，约 1.20、1.24 秒，停止原因均是深度限制，不是耗尽 8 秒。没有穷尽被束剪枝丢掉的路径。',
        '',
        '## 结构抽样的原始统计',
        '',
        '每行 48 次接受抽样。此表保留去重之前的实验统计，不应与去重后的每题平均混用；这些是刻意构造的冻结态，不是原问题的无偏随机样本。',
        '',
        '| p,n | 整数提升范围 | 两步分组预处理有证书 | 该机制未覆盖 |',
        '|---|---|---:|---:|',
    ]
    for r in structured['records']:
        lines.append('| %d,%d | ±%s | %d | %d |' %
                     (r['p'], r['n'], r['lift_bound'], r['two_preparation_steps_certified'],
                      r['outside_two_preparation_horizon']))
    lines += [
        '',
        '## 输入、输出与验解',
        '',
        '每题的 input 数组顺序就是原位置顺序。大整数用十进制字符串保存，禁止先转成 JavaScript Number 或双精度浮点数。目标是原始全局平均数；除已全等对照外，本包目标均为零。',
        '',
        '输出如下，operations 中每行恰好 p 个互不相同的 **1 基位置编号**：',
        '',
        '~~~json',
        '{"solutions":[{"case_id":"control-already-equal","operations":[]},{"case_id":"control-negative-p7-n14","status":"unreachable"}]}',
        '~~~', '',
        '对正例，只有完整原子操作序列才计为解。声称可达、给一个群元素、最终自行清分母，均不算完成；算法内部可以规范化来选组，但验解器在原值上重放索引，绝不规范化实际状态。允许恒等操作，但单独统计其数量。',
        '',
        '~~~text',
        'python verify_paths.py --self-check --output reference_audit.json',
        'python verify_paths.py --cases quick_cases.json --solutions my_solutions.json --output scores.json',
        'python generate_cases.py --p 7 --count 100 --bits 128 --seed 20260913 --output fresh_cases.json',
        '~~~', '',
        '路径验解检查每步容量、索引、精确平均与最终全等，报告操作数、首次达到目标的坐标步数、分母高度和中间分子位长。not_found 是未构造成功；只有已证阴性对照可以用 unreachable 得分。对于新生成的题，验解器仍可校验完整路径，但不把无证明的 unreachable 答案当成正确。',
        '',
        '## 建议的评分方式',
        '',
        '- 首先报告完整有效路径率、无效路径数、误报不可达数；阴性对照单独计分。',
        '- 再按 p 与提升范围分别报告时间、展开节点数、路径长度、分母最大指数、分子最大位长。',
        '- 每题至少使用两个不同搜索预算，例如 1 秒与 10 秒，同时固定内存上限、线程数和搜索策略。',
        '- 对已有参考路径的题，比较构造速度与路径长度；参考步数是上界，不自动等于最优解。',
        '- 对暂未附路径的题，第一次生成并通过验解的路径就成为新的参考；不要把旧预算失败当成下界。',
        '- 先用 quick_cases.json 做回归，再用全部题和固定新种子评估；若使用参考路径调参，应另用新种子作最终测试。',
        '',
        '时间与内存由调用算法的外部计时器记录；本验解器不声称隔离或限制资源。比较结果应写明运行设备，旧墙钟时间仅作描述。',
        '',
        '## 可继续生成同类题的公式',
        '',
        '选 3≤L≤min(p−1,6)，把 p−1 分成正整数 r₁+…+r_L；取整数提升 z_i 且 Σz_i=−3。令 x_i=1+r_i+p z_i，背景 1 取 2p+1−L 份。总和自动为零；筛 gcd(x_i−1)=1 即有 G=1。所有例外差的模 p 正代表总和为 p−1，故无非空零和子序列，整状态没有非恒等整数平均。',
        '',
        '给定种子、L 分布、提升范围和筛选规则后再比较算法，避免只保留某个算法成功或失败的样本。',
        '',
        '## 额外的历史方法回归例',
        '',
        '二十三平均七十元：' + compact(case_by_id[protected_id]) + '。五步参考已包含在主包。若固定保护 −1073，旧双锚点候选都会碰撞；重选保护位置可直接推进。这是特定选择器失败，不是全问题困难下界。',
        '',
        '另有两例不纳入主分数，可检验算法是否错误地坚持某个形式：',
        '',
        '- 五平均十二元 (14^5, (−8)^5, (−15)^2)：在旧二维除法字母族中，合法单步会把 |v| 从 11 增到 13；这个例子仅针对该下降策略，本包未附完整路径。',
        '- 六十一平均一百五十元 (0^142,16,21^4,25^2,−150)：块—单点交换无法把所有局部单位条件同时集中到一个差上，但初态有大量零，完整问题本来就可轻松收尾。它专门防止把“方法不适用”误报成“题目难解”。',
        '',
        '七平均十五元真值来源：研究目录中的 outputs/seven_average_fifteen_complete.md，核验 ID seven-average-fifteen-complete；本轮只读取并记录其范围，不重复该证明。它不自动证明 p=19,n=39 或 p=37,n=75。扩展集中 %d 道未附路径且未导入完整定理的题，其 expected_reachable 为 null，不纳入已知真值正确率。' %
            summary['extension_cases_without_ground_truth'],
        '',
        '输入文件可单独给求解器；manifest 与 reference_solutions 由评测端保管。所有文件可以离线使用，不依赖原研究目录。',
    ]
    (OUT/'README.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == '__main__':
    main()
