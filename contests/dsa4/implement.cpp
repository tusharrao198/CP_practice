#include <iostream>
#define SPACE 10
using namespace std;

class TreeNode{
    public:
        int value;
        // two pointers left and right
        TreeNode *left;
        TreeNode *right;
        // default constructors default value is set as 0
        TreeNode()
        {
            value =0;
            left = NULL;
            right = NULL;
        }
        //parameterized constructors take integer value or key or data. 
        TreeNode(int v)
        {
            value = v;
            left = NULL;
            right = NULL;
        }
};

class BST{
    public:
        TreeNode *root;
    BST()
    {
        root = NULL;
    }

    //is empty function to check if tree is empty
    bool isEmpty()
    {
        if (root==NULL)
        {
            return true;
        }   
        else
        { 
            return false;
        }   
    }

    void insertNode(TreeNode *new_node)
    {
        if (root==NULL)
        {
            root = new_node;
            cout << "value inserted as root node"<< endl;
        } 
        else
        {
            TreeNode *temp =root; // initially set as root
            while(temp!=NULL)
            {//conditions
                if (new_node->value == temp->value)
                {
                    cout << "value already exist"<< "insert another value"<< endl;
                    return ;
                }
                else if (new_node->value < temp->value) && (temp->left==NULL)
                {
                    temp->left = new_node;   
                    cout << "value inserted! at left node" << endl;
                    break;
                } 
                else if (new_node->value < temp->value)
                {
                    temp = temp->left;  // now temp set to left's pointer now we can set value to the left  
                }
                else if (new_node->value > temp->value) && (temp->right==NULL)
                {
                    temp-> right = new_node;
                    cout << "value inserted! at right node" << endl;
                    break;
                }
                else
                {
                    temp = temp->right;
                }
            }
        }
    }
    
    void print2D(TreeNode * r, int space) 
    {
        if (r == NULL) // Base case  1
            return;
        space += SPACE; // Increase distance between levels   2
        print2D(r -> right, space); // Process right child first 3 
        cout << endl;
        for (int i = SPACE; i < space; i++) // 5 
            cout << " "; // 5.1  
        cout << r -> value << "\n"; // 6
        print2D(r -> left, space); // Process left child  7
    }


};

 

















int main() {
  BST obj;
  int option, val;

  do {
        cout << "What operation do you want to perform? " <<
        " Select Option number. Enter 0 to exit." << endl;
        cout << "1. Insert Node" << endl;
        cout << "2. Search Node" << endl;
        cout << "3. Delete Node" << endl;
        cout << "4. Print/Traversal BST values" << endl;
        cout << "5. Height of Tree" << endl;
        cout << "6. Clear Screen" << endl;
        cout << "0. Exit Program" << endl;

        cin >> option;
        //Node n1;
        TreeNode * new_node = new TreeNode();

        switch (option) {
            case 0:
                break;
            case 1:
                cout << "INSERT" << endl;
                cout << "Enter VALUE of TREE NODE to INSERT in BST: ";
                cin >> val;
                new_node -> value = val;
                obj.insertNode(new_node);
                cout << endl;
                break;
            case 2:
                cout << "SEARCH" << endl;
                cout << "Enter VALUE of TREE NODE to SEARCH in BST: ";
                cin >> val;
                //new_node = obj.iterativeSearch(val);
                new_node = obj.recursiveSearch(obj.root, val);
                if (new_node != NULL) {
                    cout << "Value found" << endl;
                } else {
                    cout << "Value NOT found" << endl;
                }
                break;
            case 3:
                cout << "DELETE" << endl;
                cout << "Enter VALUE of TREE NODE to DELETE in BST: ";
                cin >> val;
                new_node = obj.iterativeSearch(val);
                if (new_node != NULL) {
                    obj.deleteNode(obj.root, val);
                    cout << "Value Deleted" << endl;
                } else {
                    cout << "Value NOT found" << endl;
                }
                break;
            case 4:
                cout << "PRINT 2D: " << endl;
                obj.print2D(obj.root, 5);
                cout << endl;
                cout << "Print Level Order BFS: \n";
                obj.printLevelOrderBFS(obj.root);
                cout << endl;
                //	      cout <<"PRE-ORDER: ";
                //	      obj.printPreorder(obj.root);
                //	      cout<<endl;
                //	      cout <<"IN-ORDER: ";
                //	      obj.printInorder(obj.root);
                //	      cout<<endl;
                //	      cout <<"POST-ORDER: ";
                //	      obj.printPostorder(obj.root);
                break;
            case 5:
                cout << "TREE HEIGHT" << endl;
                cout << "Height : " << obj.height(obj.root) << endl;
                break;
            case 6:
                system("cls");
                break;
                default:
                cout << "Enter Proper Option number " << endl;
    }

  } while (option != 0);

  return 0;
}
