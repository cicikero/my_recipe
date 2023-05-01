sub fib($) {
    return $_[0] if ($_[0] < 2);
    return fib($_[0] - 2) + fib($_[0] - 1);
}
 
print fib(38), "\n";
