#!/usr/bin/perl
# Find ONE explicit mixing sequence (position-indexed, 1-based) for a given multiset.
# BFS over exact dyadic fractions, positions kept fixed (no sorting), so the printed
# sequence can be fed straight into `checker.pl verify`.
use strict; use warnings;

my $KMAX = shift @ARGV // 10;
my @init = map { 0 + $_ } @ARGV;
my $n = @init;
my $S = 0; $S += $_ for @init;

sub reduce_fraction {
    my ($num, $e) = @_;
    while ($num != 0 && $num % 2 == 0 && $e > 0) { $num /= 2; $e--; }
    if ($num == 0) { $e = 0; }
    return ($num, $e);
}
sub key { my @v = @_; return join(",", map { $_->[0]."/".$_->[1] } @v); }
sub sorted_key { my @v = @_; my @p = map { $_->[0]."/".$_->[1] } @v; return join(",", sort @p); }
sub is_target {
    my @v = @_;
    my ($t0,$t1) = @{$v[0]};
    return 0 if $t0 * $n != $S * (1 << $t1);   # value == S/n ?
    for my $i (1 .. $n-1) { return 0 unless $v[$i][0]==$t0 && $v[$i][1]==$t1; }
    return 1;
}

my @start = map { [$_, 0] } @init;
my %seen;
my @queue = ( \@start );
$seen{ sorted_key(@start) } = "ROOT";
my %parent;   # key -> [parent_key, i, j]

my $found_key;
while (@queue) {
    my $st = shift @queue;
    my $sk = sorted_key(@$st);
    for my $i (0 .. $n-1) {
        for my $j ($i+1 .. $n-1) {
            my ($n1,$e1) = @{$st->[$i]};
            my ($n2,$e2) = @{$st->[$j]};
            my $em = $e1 > $e2 ? $e1 : $e2;
            my $a1 = $n1 * (1 << ($em-$e1));
            my $a2 = $n2 * (1 << ($em-$e2));
            my ($rn,$re) = reduce_fraction($a1+$a2, $em+1);
            next if $re > $KMAX;
            my @ns = map { [$_->[0],$_->[1]] } @$st;
            $ns[$i] = [$rn,$re];
            $ns[$j] = [$rn,$re];
            my $k = sorted_key(@ns);
            next if exists $seen{$k};
            $seen{$k} = 1;
            $parent{$k} = [$sk, $i, $j];
            if (is_target(@ns)) { $found_key = $k; last; }
            push @queue, \@ns;
        }
        last if defined $found_key;
    }
    last if defined $found_key;
}

if (!defined $found_key) { print "NOT FOUND (KMAX=$KMAX)\n"; exit 1; }

# reconstruct
my $root_key = sorted_key(@start);
my @steps;
my $k = $found_key;
while ($k ne $root_key) {
    my ($pk, $i, $j) = @{$parent{$k}};
    push @steps, [ $i+1, $j+1 ];
    $k = $pk;
}
@steps = reverse @steps;
print "multiset: @init\n";
print "steps: ", scalar(@steps), "\n";
for my $s (@steps) { print "$s->[0] $s->[1]\n"; }
