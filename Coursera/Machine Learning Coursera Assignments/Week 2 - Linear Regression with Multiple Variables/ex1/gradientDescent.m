function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
 K = 0;
for iter = 1:num_iters
    K = (1/m)*sum(X.*repmat((X*theta - y), 1, size(X,2)));
    theta = (theta' - (alpha * K))';
    J_history(iter) = computeCost(X, y, theta);
end

end
