% Sort three
disp('Sort three')
a = input('Enter first number: ');
b = input('Enter second number: ');
c = input('Enter third number: ');

if (a < b) && (a < c)
    disp(a)
    if b < c
        disp(b)
        disp(c)
    else
        disp(c)
        disp(b)
    end
elseif (b < c) && (b < a)
    disp(b)
    if a < c
        disp(a)
        disp(c)
    else
        disp(c)
        disp(a)
    end
elseif (c < a) && (c < b)
    disp(c)
    if a < b
        disp(a)
        disp(b)
    else
        disp(b)
        disp(a)
    end
end