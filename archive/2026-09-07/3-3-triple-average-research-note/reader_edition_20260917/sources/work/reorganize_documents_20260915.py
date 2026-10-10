"""Plan/apply document-only moves and repair internal links deterministically.

No source proof is deleted. Before editing, affected text is snapshotted under
work/document_reorganization_20260915/originals. Runtime modules stay in work.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
RECORD = ROOT / 'work/document_reorganization_20260915'
OUT = ROOT / 'outputs'

LOWER = set('''prime_arity_unrestricted_endpoint_and_odd_band
prime_arity_endpoint_congruence_completion prime_arity_uniform_odd_middle_cores
prime_arity_even_interior_completion prime_arity_two_p_plus_two_uniform
prime_arity_three_p_minus_one_completion prime_arity_middle_band_structure'''.split())
UPPER = set('''prime_arity_upper_band_three_value_reduction
prime_arity_upper_band_four_return_congruence prime_arity_upper_band_coprime_six_complete
prime_arity_upper_band_unrestricted_completion prime_arity_upper_band_overlap_completion
prime_arity_all_prime_three_p_plus_ten prime_arity_nine_offsets_large_symmetric_carrier_completion'''.split())
TAIL = set('''prime_arity_linear_threshold prime_arity_inverse_egz_threshold
prime_arity_four_p_tail_completion prime_arity_averaging_large_dimension'''.split())
TOOLS = set('''prime_arity_unified_weighted_core_theorem
prime_arity_interpolation_and_lattice_structure prime_power_endpoint_and_critical_geometry
uniform_endpoint_positive_controller'''.split())
STRUCTURE = set('''prime_arity_binary_collision_lattice prime_arity_complete_unit_collision_recovery
prime_arity_critical_structures prime_arity_energy_and_dyadic_neighbour
prime_arity_invariant_improvements_and_core_exit prime_arity_middle_band_relative_scale
prime_arity_provenance_dynamic_and_integer_stages prime_arity_shape_changing_integer_potential
prime_arity_shape_potential_literature_interface prime_arity_sharp_repetition_and_precision_barriers
prime_arity_single_value_zero_sum_conjecture prime_arity_uniform_collision_structure'''.split())
TRIPLE_PROOFS = set('''triple_average_all_dimensions_double_triple_invariant
triple_average_all_dimensions_to_primes triple_average_prime_double_triple_invariant
triple_average_seven_eight_complete triple_average_ten_complete
triple_average_two_three_smooth_complete'''.split())
ALGORITHM = set('''averaging_algorithm_benchmark arena_triple_solver_review
pair_triple_solver_comparison_and_optimality triple_average_sequence_length_analysis
triple_average_computation_performance_audit triple_average_search_optimization_review_2026-09-09
triple_average_verification_guide'''.split())
LITERATURE = set('''averaging_literature_survey_2018_2026
triple_average_binary_source_reassessment_2026-09-11 binary_vs_ternary_averaging_followup'''.split())
GENERAL = set('''averaging_global_status_20260912 averaging_proof_strategy_and_composite_frontier_20260915
arbitrary_arity_linear_threshold ht_literature_and_eventual_square_completion_20260915
large_prime_high_odd_power_three_step_reflections square_arity_uniform_controller_and_nine_thirteen
two_three_odd_power_critical_grh_completion ten_average_sixteen_and_dyadic_network_family
ten_twelve_average_seventeen_complete inverse_zero_sum_averaging_progress
triple_average_q_average_arithmetic_geometry'''.split())

def category(path):
    s = path.stem
    if path.name == 'README.md': return None
    if s in LOWER: return 'prime_arity/proofs/lower_band'
    if s in UPPER: return 'prime_arity/proofs/upper_band'
    if s in TAIL: return 'prime_arity/proofs/tail_and_lower_bound'
    if s in TOOLS: return 'prime_arity/tools'
    if s in STRUCTURE: return 'prime_arity/structure'
    if s.startswith('prime_arity_'):
        return 'prime_arity/audits' if 'audit' in s else 'prime_arity/history'
    if s in ALGORITHM: return 'algorithms'
    if s in LITERATURE: return 'literature'
    if s.startswith(('general_k_', 'composite_', 'even_arity_', 'odd_composite_')) or s in GENERAL:
        return 'general_arity'
    if s.startswith(('four_average_', 'six_average_')): return 'general_arity/examples'
    if s.startswith(('five_average_', 'seven_average_', 'seven_exact_', 'p13_')):
        return 'prime_arity/examples'
    if s in TRIPLE_PROOFS: return 'triple_average/proofs'
    if s.startswith('triple_average_') and s.endswith('_complete'):
        return 'triple_average/arithmetic_cases'
    if s.startswith(('triple_average_', 'ternary_', 'ai3_')): return 'triple_average/history'
    if s.startswith('research_'): return 'history'
    raise ValueError('Unclassified document: ' + path.name)

def plan():
    moves = {}
    for old in sorted(OUT.glob('*.md')):
        folder = category(old)
        if folder:
            moves[old.relative_to(ROOT).as_posix()] = (Path('outputs') / folder / old.name).as_posix()
    return moves

def main():
    RECORD.mkdir(exist_ok=True)
    if '--apply' not in sys.argv:
        moves = plan()
        (RECORD / 'path_map.json').write_text(json.dumps(moves, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        counts = {}
        for dst in moves.values():
            key = str(Path(dst).parent)
            counts[key] = counts.get(key, 0)+1
        print(json.dumps({'moves':len(moves),'folders':counts},ensure_ascii=False,indent=2))
        return
    moves = json.loads((RECORD / 'path_map.json').read_text(encoding='utf-8'))
    if (RECORD / 'migration_report.json').exists():
        raise RuntimeError('Migration already applied; do not run twice.')
    resolved = {}
    for old,new in moves.items():
        src,dst=(ROOT/old).resolve(),(ROOT/new).resolve()
        # Every resolved source/destination must remain under outputs.
        src.relative_to(OUT.resolve());dst.relative_to(OUT.resolve())
        assert src.is_file() and not dst.exists(), (src,dst)
        resolved[src]=dst
    suffixes={'.md','.json','.py','.txt','.tex','.html','.toml','.yaml','.yml'}
    files=[p for p in ROOT.rglob('*') if p.is_file() and p.suffix in suffixes
           and RECORD not in p.parents and p.stat().st_size<12_000_000]
    link=re.compile(r'(!?\[[^\]\n]*\]\()([^\)\n]+)(\))')
    refs=[];changed=0
    absolute_root=ROOT.as_posix()
    for oldfile in files:
        try:original=oldfile.read_text(encoding='utf-8')
        except UnicodeDecodeError:continue
        newfile=resolved.get(oldfile.resolve(),oldfile)
        def rewrite(match):
            target=match[2];wrapped=target.startswith('<') and target.endswith('>')
            raw=target[1:-1] if wrapped else target
            if re.match(r'(?i)(https?://|mailto:|app:|codex:|data:)',raw):return match[0]
            pathpart,sep,anchor=raw.partition('#')
            if not pathpart:return match[0]
            decoded=unquote(pathpart).replace('\\','/')
            if decoded.startswith('/C:/'):decoded=decoded[1:]
            absolute=bool(re.match(r'^[A-Za-z]:/',decoded))
            candidate=(Path(decoded) if absolute else oldfile.parent/decoded).resolve()
            destination=resolved.get(candidate,candidate)
            if newfile==oldfile and destination==candidate:return match[0]
            if not candidate.exists() and candidate not in resolved:
                refs.append({'source':str(oldfile.relative_to(ROOT)),'preexisting_missing':raw})
            newpath=destination.as_posix() if absolute else Path(os.path.relpath(destination,newfile.parent)).as_posix()
            replacement=newpath+(sep+anchor if sep else '')
            if wrapped:replacement='<'+replacement+'>'
            return match[1]+replacement+match[3]
        updated=link.sub(rewrite,original) if oldfile.suffix in {'.md','.tex'} else original
        # Project-relative paths in manifests, code literals, prose, and HTML.
        for old,new in moves.items():
            updated=updated.replace(old,new)
            updated=updated.replace(old.replace('/','\\\\'),new.replace('/','\\\\'))
        if oldfile.resolve() in resolved or updated!=original:
            backup=RECORD/'originals'/oldfile.relative_to(ROOT)
            backup.parent.mkdir(parents=True,exist_ok=True)
            backup.write_bytes(oldfile.read_bytes())
            newfile.parent.mkdir(parents=True,exist_ok=True)
            newfile.write_text(updated,encoding='utf-8')
            changed+=1
        if oldfile.resolve() in resolved:
            # The new file and the exact backup have both been written already.
            assert newfile.is_file() and backup.is_file()
            oldfile.unlink()
    report={'moved_documents':len(moves),'edited_or_moved_text_files':changed,
            'path_map':'work/document_reorganization_20260915/path_map.json',
            'backup_root':'work/document_reorganization_20260915/originals',
            'preexisting_missing_links_seen':refs,
            'scope':'Documents moved; Markdown destinations and project-relative textual references rewritten. Original runtime Python modules stay in work.'}
    (RECORD/'migration_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='preexisting_missing_links_seen'},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
