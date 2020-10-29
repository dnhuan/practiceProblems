% Middle of three
disp('Middle of three')
a = input('Enter first number: ');
b = input('Enter second number: ');
c = input('Enter third number: ');
if ((a > b) && (a < c)) || ((a > c) && (a < b))
    disp(a)
elseif ((b > c) && (b < a)) || ((b > a) && (b < c))
    disp(b)
elseif ((c > a) && (c < b)) || ((c > b) && (c < a))
    disp(c)
end