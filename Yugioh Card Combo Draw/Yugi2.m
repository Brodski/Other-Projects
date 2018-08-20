function [ chance ] = Yugi2(monsters, deck )
%UNTITLED2 Summary of this function goes here
%This bad boy calculates the probablity of have x of the same card.
%   Detailed explanation goes here
chance = zeros(1,deck)
for k = monsters:deck
b = nchoosek(deck, k) %the number of ways to draw a hand on turn 1, 2, 3...
a = nchoosek(deck-monsters, k-monsters) %the number of ways to NOT draw
                                        %the desired number of monsters
chance(k) = a / b;

end
disp('Chance = ')
chance
plot(chance)
end
