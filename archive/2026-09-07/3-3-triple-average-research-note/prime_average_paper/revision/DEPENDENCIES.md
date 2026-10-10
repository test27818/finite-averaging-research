# 命题依赖与审查接口

以下使用LaTeX稳定标签。每项需按所列输出核对，不以“标签已定义”代替前提审核。

| 使用处 | 直接前提 | 必须取得的输出 |
|---|---|---|
| lem:deep | thm:arithmetic-external | D>1；两条完整hR根；不是只有有限模像 |
| lem:transverse | lem:deep | J及逆已实现，c与det J非零，计入g的三次层损失 |
| lem:content | lem:fiber | 先有整数Gamma(q)；条目本原；det与q互素 |
| thm:terminal | lem:content、cor:finite-group、lem:small-units、lem:fiber | L(delta n Z)、Gamma((delta n)^2)、粗平移、有限尺度及足够连续终端 |
| lem:integer-range | lem:initialize、lem:egz、lem:background、lem:heavy、lem:two-heavy | 安全整数续步或显式终端；整数能量严格下降 |
| prop:threep | lem:obstruction及文内三阶运输、四陪集表 | 不调用临界带判据；合法任意输入到全零 |
| lem:zero-tail | lem:zero-base、prop:threep、lem:integer-range | 包含全部非零位置且含零的局部零和子系统 |
| prop:entry | lem:short-choice、lem:concentrate、lem:two-block-entry、lem:shape-change | 在全部原位置形成合法(p,p,r)；p=3仅用n=7分支 |
| prop:odd | lem:localize、lem:deep、thm:terminal | 无穷单位环，全部上根、n下根、深核；奇行列式内容给2 |
| lem:two-carrier | lem:deep、lem:fiber | 两次CRT选数字确保真实本原输出和第二坐标±1 mod q |
| lem:even-core | lem:inverse、lem:localize、lem:binary-depth、lem:local-cycle、thm:terminal | t奇及两边界直接2n深核收尾；t偶三反射分支保留方向与尺度 |
| lem:upper-boundary | lem:inverse、lem:localize、thm:terminal | p>=7的2n根；p=5夹乘反演3后取得28根 |
| cor:resource | lem:count-interface、lem:transverse、thm:terminal | alpha gcd为1、H gcd=delta；实际倍率生成D>1环 |
| prop:upper | prop:entry、lem:upper-supply、lem:upper-small、lem:small-supply | p>=83所有上半带；小p分别s<=9、s>=10覆盖 |
| prop:wide | lem:integer-range、lem:concentrate、lem:local-cycle、lem:inverse、lem:fiber | 仅补4p+s、omega(n)>=s+3；最终调用已独立完成的4p |
| lem:collision-small | 整数下降基本引理、prop:collision-certificate | 任意有理轻值的完整线性解集；私人素数总和矛盾 |
| lem:seven22 | prop:entry转换前核心、prop:seven-certificate、lem:deep、lem:fiber | 模9满群接已有81M核；完整方向与尺度共3872状态 |
| lem:ten | 安全下降与六重桥、prop:ten-certificate | 精确二次覆盖；X=0后调用独立九元网络 |
| sec:completion | 上列命题 | p=3、5、7单列，p>=11全部覆盖；无相邻维数内插 |

## 局部化条件

- 奇数反射：f0、f1互素且奇偶相反，所以|f0 f1|>1；所有因子与n互素。
- 偶数内部：d、d+n为相差n的互素奇数，乘积绝对值>1；后加p及t的奇部有对应逆构造。
- 相邻输出通用接口：g-f=alpha n，且f与n互素，故约分倍率不为±1，得到无限单位。
- r=p-1和宽尾部：相邻标量互素且差非零大于2；每次新增数字由安全返回逆及共轭扩环，保持相同深核。
- 七平均22元：R=Z[1/35]；五平均14元：显式R先为Z[1/(5·11·13)]，再通过夹乘加入3。

本表是编辑复核清单，不是形式化证明或独立审稿报告。
