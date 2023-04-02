#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
using namespace std;

template <class T>
class Stack{
  private:
    int top = 0;
    int size;
    T* array;
  public:
    Stack(int size){
      this->size = size;
      array = new T[size];
    }

    bool isEmpty(){
      return top == 0;
    }

    bool isFull(){
      return top >= size - 1;
    }

    void push(T x){
      if(isFull()){
        throw out_of_range("値を追加できません");
      }
      top++;
      array[top] = x;
    }

    T pop(){
      if(isEmpty()){
        throw out_of_range("配列の中が空です");
      }
      top--;
      return array[top + 1];
    }
};

int main(void){
  Stack<int> stack(101);

  string str;
  getline(cin, str);
  istringstream S(str);
  int tmp = 0;

  while(!S.eof()){
    string s;
    S >> s;
    switch(s[0]){
      case '+':
        tmp = stack.pop();
        tmp += stack.pop();
        break;
      case '-':
        tmp = -(stack.pop());
        tmp += stack.pop();
        break;
      case '*':
        tmp = stack.pop();
        tmp *= stack.pop();
        break;
      default:
        tmp = stoi(s);
    }
    stack.push(tmp);
  }

  cout << stack.pop() << endl;
}
