#!/usr/bin/perl
# Reference checker for the "averaging-to-equalize" benchmark.
# No dependencies (Perl core only).
#
# Usage:
#   perl checker.pl judge            # read a multiset, print YES/NO
#   perl checker.pl verify           # read a multiset + sequence, simulate & verify
#
# Input format (stdin):
#   judge:
#     n
#     a_1 a_2 ... a_n            (n integers, may repeat, may be negative)
#
#   verify:
#     n
#     a_1 a_2 ... a_n
#     m
#     i_1 j_1
#     ...
#     i_m j_m                    (1-based indices)
#
# Note: values are kept as exact dyadic rationals  num/2^e  (the operation only ever
# introduces factors 1/2). This reference uses native integers, so it is meant for
# moderate inputs; if |numerator| would exceed ~2^50 it aborts with a clear message.
use strict; use warnings;

my $MODE = shift @ARGV // 'judge';

sub gcd { my ($a,$b)=@_; $a=abs($a); $b=abs($b); ($a,$b)=($b,$a%$b) while $b; return $a; }

sub reduce_fraction {
    my ($num, $e) = @_;
    while ($num != 0 && $num % 2 == 0 && $e > 0) { $num /= 2; $e--; }
    if ($num == 0) { $e = 0; }
    return ($num, $e);
}

my $MAXBITS = 50;
sub guard {
    my $x = shift;
    die "checker.pl: numerator too large (overflow risk). Use a big-int implementation.\n"
        if abs($x) >= (1 << $MAXBITS);
}

my $n = <STDIN>; die "missing n\n" unless defined $n; chomp $n;
my $line = <STDIN>; chomp $line;
my @a = split /\s+/, $line;
die "expected $n numbers\n" unless @a == $n;
my $S = 0; $S += $_ for @a;

if ($MODE eq 'judge') {
    # ---- n <= 2 : always YES ----
    if ($n <= 2) { print "YES\n"; exit 0; }

    # ---- n == 3 : YES iff the three numbers form an arithmetic progression ----
    if ($n == 3) {
        my @b = sort { $a <=> $b } @a;
        print ( (2*$b[1] == $b[0]+$b[2]) ? "YES\n" : "NO\n" );
        exit 0;
    }

    # ---- n >= 4 : G criterion ----
    # normalized deviations e_i = (n*a_i - S) / g, gcd(e)=1
    my @e = map { $n*$_ - $S } @a;
    my $g = 0; $g = gcd($g, $_) for @e;
    if ($g == 0) { print "YES\n"; exit 0; }          # all a_i equal
    @e = map { $_ / $g } @e;
    # G = gcd of all pairwise differences = gcd(e_i - e_1)
    my $G = 0;
    for my $i (1 .. $n-1) { $G = gcd($G, $e[$i] - $e[0]); }
    # G is a power of two <=> mixable
    my $is_pow2 = ($G == 0) ? 0 : (do { my $x = $G; while ($x % 2 == 0) { $x /= 2; } ($x == 1 ? 1 : 0); });
    print ($is_pow2 ? "YES\n" : "NO\n");
    exit 0;
}

if ($MODE eq 'verify') {
    my $m = <STDIN>; chomp $m;
    my @v = map { [$_, 0] } @a;                       # (num, e): value = num/2^e
    for my $step (1 .. $m) {
        my $l = <STDIN>; die "missing step\n" unless defined $l; chomp $l;
        my ($i, $j) = split /\s+/, $l;
        die "bad indices\n" unless 1 <= $i && $i <= $n && 1 <= $j && $j <= $n && $i != $j;
        $i--; $j--;
        my ($n1,$e1) = @{$v[$i]};
        my ($n2,$e2) = @{$v[$j]};
        my $emax = $e1 > $e2 ? $e1 : $e2;
        my $a1 = $n1 * (1 << ($emax - $e1));
        my $a2 = $n2 * (1 << ($emax - $e2));
        my $sum = $a1 + $a2;
        my ($rn, $re) = reduce_fraction($sum, $emax + 1);
        guard($rn);
        $v[$i] = [$rn, $re];
        $v[$j] = [$rn, $re];
    }
    # all equal and equal to S/n ?
    my $all_eq = 1;
    for my $i (1 .. $n-1) {
        if ($v[$i][0] != $v[0][0] || $v[$i][1] != $v[0][1]) { $all_eq = 0; last; }
    }
    # check value == S/n :  num/2^e == S/n  <=>  num*n == S*2^e
    my ($fn, $fe) = @{$v[0]};
    my $at_mean = ($fn * $n == $S * (1 << $fe)) ? 1 : 0;
    print "final state: ", join(" ", map { $_->[0] . "/2^" . $_->[1] } @v), "\n";
    print "steps=$m mean=$S/$n ";
    print (($all_eq && $at_mean) ? "VERIFIED: all equal to the mean\n" : "FAIL: not all equal to the mean\n");
    exit 0;
}

die "unknown mode '$MODE' (use judge or verify)\n";
