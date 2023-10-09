% когда tail будет пустым, в sum1 будет лежать ноль
sum_list([], 0).

% список поделили на голову и хвост, sum - это переменная
% функция вызывает сама себя (рекурсия), когда рекурсия закончится, в sum1 начнут прибавляться все головы и мы получим сумму всех элементов

sum_list([Head|Tail], Sum) :-
    sum_list(Tail, Sum1),       
    Sum is Head + Sum1.        

?- sum_list([1, 2, 3, 4, 5, 25], X).
domains