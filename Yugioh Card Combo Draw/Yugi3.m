
function [ chance ] = Yugi3(monsters, deck, x)
%UNTITLED2 Summary of this function goes here
%This bad boy calculates the probablity of have x number of the same card.
%   It uses combinatorics, n choose k, and order does not matter
%   ie, draw 2 CardXs by your 10th draw.
%
%   x (in the parameter) is the number which we're question "what are the 
%	chances of drawing x many cards"
%        x number of monsters (CardXs) by the n-th drawn card
%
%   Chanceing of drawing x number of CardXs by turn n 
%           = (number of ways to draw at least x of the same card) / 
%                     (number of ways to draw "10" cards from your deck)
%
%   monsters > x (obviously)

% In order to calculate the number of ways to draw x number of monsters out
%  of some number of monsters, we must calculate the number of ways to draw
%  x monsters and drawncards-x monsters, then x+1 monsters and
%  drawncards-(x+1)monsters, then x-2 monsters... 
%
%Example,by the 5th card;  
%  We find the number of ways to draw 2 monsters when we have 4 monsters in deck, 
%  and draw 3 others cards that are not monsters. 
%  Then find number of ways to draw 3 monsters (when we have 4 monsters) 
%  and draw 2 other cards that are not monters. Ect.

%Set up arrays
chance = zeros(1,deck);
a = zeros(1,1+monsters-x);

for k = x:deck-monsters
%the number of ways to draw a hand on turn 1, 2, 3..., k is:
b = nchoosek(deck, k); 

%if the number of drawn cards is less then our monsters in the deck we 
% skip down.
    if k >= monsters
        
    %first i is the number of ways to draw 4 monsters, then 3
    %monsters then 2 monsters
    %Since  monsters > x, we must account for the draws in which we
    %draw more than x
       for i = 0:(monsters - x) 
   
         combx    = nchoosek(monsters, x+i); %number of ways to draw monsters
         combNotx = nchoosek(deck-monsters, k-x-i);%number of ways to not draw monsters
         a(i+1)   = combx*combNotx; %the number of ways to draw x 
       
       end
    else
        for i = 0:(k-x)
            combx = nchoosek(monsters, x+i);
            combNotx = nchoosek(deck-monsters, k-x-i);
            a(i+1) = combx*combNotx;
        end
    end
    
chance(k) = sum(a) / b; %total
end
disp('chance of drawing x number of the same card is')
chance
plot(chance)
end


%
%   http://www.nandor.org/math/ProbStats/Discrete/countingbasics/countingbasics.htm
%
