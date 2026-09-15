"""Register the current four bounded verification interfaces."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
manifest_path=root/'work/verification_manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
specs=[
 ('two-three-odd-power-critical',
  'Under Dirichlet GRH, every k=m*s^2,n=k+m*s+1 with m in{2,3},s>=2 has the complete G=1 criterion. This proves all2/3 odd-exponent critical points; combined with the square family, all powers of2 and3 reach their conjectured first critical dimension.',
  'proved-two-three-square-multiple-dimensions-and-odd-power-critical-points-under-GRH',
  'outputs/general_arity/two_three_odd_power_critical_grh_completion.md',
  'work/verify_two_three_odd_prime_power_critical.py',
  ['two-three odd-power uniform controller and entry identities: PASS 24','two-three odd-power literal cyclic and multiplier returns: PASS 32','two-three odd-power forced singleton-entry replay: PASS 2','two-three odd-power complete finite small-unit certificates: PASS 11','two-three square-multiple full finite small-unit certificates: PASS 508','two-three odd-prime-power critical completion interfaces: PASS'],
  'Exact C^4/C^6 cycles, the uniform two-step identity M_d=C^2*Delta(d), inverse sandwiches and complete root groups are proved by formulas. Full input entry uses a three-singleton commutator with no failing prime. The complete508-case unit certificates cover2<=s<256; GRH covers all larger s. Checks also replay32 physical returns and2 forced entry paths.',
  'Does not prove optimal final N, general p>=5 odd-power critical points, or all mixed arities. Some mixed square multiples are solved at a dimension above their conjectured first threshold.',
  ['work/two_three_square_multiple_small_units.json','work/two_three_odd_power_small_units.json']),
 ('even-arity-all-endpoints',
  'Every even arity k>=2 has the full G=1 criterion in dimension2k+1. Together with the established odd-arity endpoint theorem, all integer arities now have the2k+1 endpoint. Uses the old even seed plus a uniform inverse sandwich, full dyadic roots and small balanced unit representatives.',
  'proved-all-even-arity-endpoints-with-stated-Morris-Serre-dependencies',
  'outputs/general_arity/even_arity_all_endpoints_completion.md',
  'work/verify_even_arity_endpoint_uniform.py',
  ['even-arity uniform endpoint roots and inverse formulas: PASS 199','even-arity literal full-system scalar cycles: PASS 26','even-arity all-parameter endpoint interfaces: PASS'],
  'Written proof covers both parity classes of k/2, actual scalar cycles, positive inverse activation, root groups, all units mod2k+1, full input entry and precise terminal.199 arity checks and26 literal cycles audit formulas; they do not replace all-arity quantifiers.',
  'Does not prove N(k)<=2k+1 or the conjectured composite first critical threshold. No uniform path complexity or shortest solution claim.',[]),
 ('ten-sixteen-dyadic-network-family',
  'For b>=1,k=2(4^b-1)/3,n=4^b, a fixed2b+2-step original-position k-average network averages every real input. In particular ten-average16 positions admits a six-step network and M(10)=16, while H(10)=17 was already proved.',
  'proved-fixed-network-family-and-ten-average-sixteen-first-success',
  'outputs/general_arity/ten_average_sixteen_and_dyadic_network_family.md',
  'work/verify_dyadic_three_block_fixed_network.py',
  ['dyadic three-block fixed networks exact basis: PASS 84','dyadic three-block general recurrence: PASS 40','ten-average sixteen-position universal six-step network: PASS'],
  'The three equal-block recurrence has a closed rational formula matching global mean at step2b-1, followed by a global-sum cleanup.84 exact basis columns for4,16,64 positions certify the fixed networks;40 recurrence instances check the written identity. No word search.',
  'Does not prove six steps optimal, N(10)=16, or that every network-family dimension is the minimal threshold for its arity.',[]),
 ('odd-composite-coprime-middle-band',
  'For odd integers k,r with1<=r<k and gcd(k,r)=1, dimension2k+r has the complete G=1 criterion. For every odd prime power k=p^a, all odd2k<n<3k satisfy the complete p-supported G criterion, including shared p factors, by exact nonuniform-block-mean transfer.',
  'proved-odd-composite-coprime-band-and-all-odd-prime-power-odd-middle-dimensions',
  'outputs/general_arity/odd_composite_coprime_middle_band_completion.md',
  'work/verify_odd_composite_coprime_band.py',
  ['odd-composite coprime-band exact algebra and terminal interfaces: PASS 144 114','odd-prime-power band divisor reduction identities: PASS 9894','odd-composite coprime-band extension interfaces: PASS'],
  'The proof reviews each use of primality in the old odd-band argument and replaces it with actual coprimality and short-sieve capacity.144 composite systems,114 literal returns and432 terminal transports verify formulas;9894 divisor reductions verify prime-power arithmetic. Full entry and conditional equal-block simulation are supplied by written proofs.',
  'Does not solve even dimensions, all mixed-arity noncoprime bands, general odd-power critical points or final thresholds.',[]),
]
new=[]
for id,claim,status,doc,script,markers,scope,limits,support in specs:
    entry={'id':id,'claim':claim,'claim_status':status,'evidence_level':'theorem-certificate' if support or id=='ten-sixteen-dyadic-network-family' else 'symbolic-check',
        'documents':[doc],'scripts':[script],'commands':[{'argv':['python',script],'expected_markers':markers}],
        'evidence_scope':scope,'does_not_establish':limits,'runtime_class':'short',
        'dependencies':['Python standard library and existing exact Fraction/Ledger primitives',
            'Explicitly cited original-position entry, root and terminal lemmas'+('; Dirichlet GRH, Morris/Serre and finite-ring inverses' if id=='two-three-odd-power-critical' else '; Morris/Serre where specified in the proof')],
        'profiles':['core','full']}
    new.append(entry)
    for path in support:
        if not any(x['path']==path for x in manifest['referenced_support_files']):
            manifest['referenced_support_files'].append({'path':path,'documents':[doc],
                'role':'Complete finite small-parameter unit-group rank witnesses; all remaining parameters covered by written GRH bound.',
                'authority':'Finite abelian quotient certificate, not a standalone all-input or unbounded-parameter proof.'})
ids={x['id'] for x in new}
manifest['verifications']=new+[x for x in manifest['verifications'] if x['id'] not in ids]
manifest['composite_mainline_latest']='GRH mainline now includes all2^a and3^a first critical points, plus k=2s^2/3s^2 dimensions; all integer arities have2k+1 endpoints; ten-average16 has a fixed six-step network; all odd middle dimensions for odd prime-power arity are solved. General higher odd powers of primes>=5, mixed critical points and full interval continuation remain open.'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('registered GRH mainline verification interfaces:',len(new))
