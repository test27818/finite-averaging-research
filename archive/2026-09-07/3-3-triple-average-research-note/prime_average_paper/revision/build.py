"""Assemble native LaTeX and numerical certificate tables; no text conversion."""
import ast
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent
ROOT = PREVIOUS.parent
PARTS = ['preamble.tex', '01_problem.tex', '02_obstruction.tex', '03_arithmetic.tex',
         '04_descent.tex', '05_blocks.tex', '06_compression.tex', '07_controllers.tex',
         '08_wide.tex', '09_completion.tex', 'appendix_lower.tex', 'appendix_upper.tex',
         'appendix_small.tex', 'appendix_certificates.tex', 'references.tex']


def put(path, text):
    path.write_text(text, encoding='utf-8', newline='\n')


def table_from_previous(name, caption, label):
    text = (PREVIOUS/name).read_text(encoding='utf-8')
    start = text.index(r'\begin{longtable}')
    end = text.index(r'\end{longtable}', start) + len(r'\end{longtable}')
    table = text[start:end]
    pos = table.index('\n')
    table = table[:pos] + '\n' + r'\caption{' + caption + r'}\label{' + label + r'}\\' + table[pos:]
    return r'\begingroup\small'+'\n'+table+'\n'+r'\endgroup'


def fraction(value):
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return r'\frac{' + str(value.numerator) + '}{' + str(value.denominator) + '}'


def tuple_math(values):
    return '(' + ','.join(map(fraction, values)) + ')'


def collision_tables():
    tree = ast.parse((PREVIOUS/'finite_checks.py').read_text(encoding='utf-8'))
    data = {n.targets[0].id: ast.literal_eval(n.value) for n in tree.body
            if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name)
            and n.targets[0].id in ('FIVE_TABLE', 'SEVEN_TABLE')}
    five = [r'\begingroup\small', r'\begin{longtable}{rrrlll}',
            r'\caption{五平均的全部相容系统}\label{tab:five-data}\\',
            r'\toprule $c$&$\alpha$&$\beta$&余数列&唯一解&$D$\\\midrule\endhead']
    for a,b,c,residues,values in data['FIVE_TABLE']:
        mass=5+a+sum(map(Fraction,values))
        five.append(f'{c}&{a}&{b}&${tuple_math(residues)}$&${tuple_math(values)}$&${fraction(mass)}$'+r'\\')
    five += [r'\bottomrule\end{longtable}\endgroup']
    seven=[r'\begingroup\small', r'\begin{longtable}{rrrllll}',
           r'\caption{七平均的全部相容系统}\label{tab:seven-data}\\',
           r'\toprule $e$&$\alpha$&$\beta$&余数&重数&唯一解&$D$\\\midrule\endhead']
    for e,a,b,residues,counts,values in data['SEVEN_TABLE']:
        mass=7+a+sum(Fraction(v)*f for v,f in zip(values,counts))
        seven.append(f'{e}&{a}&{b}&${tuple_math(residues)}$&${tuple_math(counts)}$&${tuple_math(values)}$&${fraction(mass)}$'+r'\\')
    seven += [r'\bottomrule\end{longtable}\endgroup']
    return '\n'.join(five+seven)


def main():
    text = '\n'.join((HERE/name).read_text(encoding='utf-8') for name in PARTS)
    text = text.replace('% ROOT_TABLE', table_from_previous('certificate.tex', '114组参数的相邻反射计数', 'tab:root-data'))
    text = text.replace('% TEN_TABLE', table_from_previous('ten_cover.tex', '十二个二次覆盖：$i:(a,b,c)$ 表示 $a+bt+ct^2>0$', 'tab:ten-data'))
    text = text.replace('% COLLISION_TABLES', collision_tables())
    text = re.sub(r'(\\caption\{[^\n]*\n)(.*?)(\\endhead)',
                  lambda m: m[1]+m[2]+r'\endfirsthead'+'\n'+m[2]+m[3], text, flags=re.S)
    cited = set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', text))
    # Labels with no incoming reference do not belong in the deliverable.
    text = re.sub(r'\\label\{([^}]+)\}', lambda m: m[0] if m[1] in cited else '', text)
    put(HERE/'prime_average_revised.tex', text)
    shutil.copyfile(PREVIOUS/'finite_checks.py', HERE/'finite_checks.py')
    shutil.copyfile(ROOT/'research/prime_arity_padic/conservation_remaining_root_cases.json', HERE/'root_certificate.json')
    manifest = {name: sha256((HERE/name).read_bytes()).hexdigest() for name in PARTS}
    put(HERE/'source_manifest.json', json.dumps(manifest,indent=2)+'\n')
    labels=re.findall(r'\\label\{([^}]+)\}',text)
    refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',text)
    report={'main_sections':text.split(r'\appendix')[0].count(r'\section{'),
            'appendix_sections':text.split(r'\appendix')[1].count(r'\section{'),
            'formal_statements':sum(text.count('\\begin{'+name+'}') for name in ('lemma','theorem','proposition','corollary','definition')),
            'labels':len(labels),'references':len(refs),
            'missing_references':sorted(set(refs)-set(labels)),
            'unused_labels':sorted(set(labels)-set(refs)),
            'duplicate_labels':sorted({x for x in labels if labels.count(x)>1}),
            'forbidden_commands':{s:text.count(s) for s in (r'\ensuremath',r'\texorpdfstring',r'\addcontentsline',r'\subsection*',r'\tag{')},
            'lines':len(text.splitlines())}
    put(HERE/'structure_check.json', json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if report['missing_references'] or report['duplicate_labels'] or any(report['forbidden_commands'].values()):
        raise SystemExit(1)


if __name__=='__main__':
    main()
