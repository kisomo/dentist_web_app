#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;
/*
using std::cout; using std::cin;
using std::endl; using std::string;
using std::vector; using std::istringstream;
using std::stringstream;
*/

int main()
{
   fstream newfile1, newfile2; 
  
   newfile1.open("address_test.txt",ios::in); // read
   if (newfile1.is_open()) 
   {
      string tp;
      while(getline(newfile1, tp)) 
        { //cout << tp << "\n"; 
            newfile2.open("address_test_out.txt",ios::out); // write
            if(newfile2.is_open()) 
            { newfile2<< tp << endl;newfile2<< " " << endl; }
        } 
      newfile2.close(); 
      newfile1.close(); 
   }


   return 0;
}

