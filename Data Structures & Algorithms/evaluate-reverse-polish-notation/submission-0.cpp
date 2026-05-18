class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<string> s;
        for (int i = 0; i < tokens.size();i++)
        {
            int temp = 0;
            if (tokens[i] == "+")
            {
                int temp2 = stoi(s.top());
                s.pop();
                int temp1 = stoi(s.top());
                s.pop();
                int temp = temp1 + temp2;
                s.push(to_string(temp));
            }
            else if (tokens[i] == "-")
            {
                int temp2 = stoi(s.top());
                s.pop();
                int temp1 = stoi(s.top());
                s.pop();
                int temp = temp1 - temp2;
                s.push(to_string(temp));
            }
            else if (tokens[i] == "*")
            {
                int temp2 = stoi(s.top());
                s.pop();
                int temp1 = stoi(s.top());
                s.pop();
                int temp = temp1 * temp2;
                s.push(to_string(temp));
            }
            else if (tokens[i] == "/")
            {
                int temp2 = stoi(s.top());
                s.pop();
                int temp1 = stoi(s.top());
                s.pop();
                int temp = temp1 / temp2;
                s.push(to_string(temp));
            }
            else 
            {
                s.push(tokens[i]);
            }

        }
        return stoi(s.top());
    }
};
