% Prime
disp('Prime')
n = input('Enter number: ');
flag = false;
for i=2:fix(n/2)
    if(mod(n,i) == 0)
        flag = true;
    end
end
if (n == 0) || (n == 1)
    flag = true;
end
if(flag)
    disp('Not Prime')
else
    disp('Prime')
end