#include <iostream>
using namespace std;

struct Node {
	int data;  // used for holding the key
	Node *parent;  // creating a pointer to the parent
	Node *left;     // creating a pointer to left child
	Node *right; // creating a pointer to right child
	int color;   // initializing color with 1 as 'Red', and 0 as 'Black'
};

typedef Node *NodePtr;

// creating class RBTree to implement the operations in Red Black Tree
class RBTree {
private:
	NodePtr root;
	NodePtr TNULL;
	// First , to initialize the nodes with appropriate values
	// Initially all the pointers are set to point to the null pointer
	void initializeNULLNode(NodePtr node, NodePtr parent) {
		node->data = 0;
		node->left = nullptr;   // initially null pointer
		node->parent = parent;
		node->right = nullptr;   // initially null pointer
		node->color = 0;
	}
    // preOrder helper function in a sequence of node [ root, left, right]
	void preOrderHelper(NodePtr node) {
		if (node != TNULL) {
			cout<<node->data<<" ";
			preOrderHelper(node->left);
			preOrderHelper(node->right);
		}
	}
    // inOrder helper function in a sequence of node [ left, root, right]
	void inOrderHelper(NodePtr node) {
		if (node != TNULL) {
			inOrderHelper(node->left);
			cout<<node->data<<" ";
			inOrderHelper(node->right);
		}
	}
    // postOrder helper function , in a sequence of node[left, right, root]
	void postOrderHelper(NodePtr node) {
		if (node != TNULL) {
			postOrderHelper(node->left);
			postOrderHelper(node->right);
			cout<<node->data<<" ";
		}
	}
    // search tree helper to search if a node is present or not.
	NodePtr searchTreeHelper(NodePtr node, int key) {
		if (node == TNULL || key == node->data) {
			if (key == node-> data){             // if node found
                    cout << "\nNode = "<< key << " found"<<endl;
                    return node;
            }else{                           // if node not found
                cout << "\nNode = "<<key << " not present"<<endl;
                return node;
                }
		}
		if (key < node->data) {
			return searchTreeHelper(node->left, key);
		}
		return searchTreeHelper(node->right, key);
	}

	// update the rb tree modified by the delete operation
	void delete_update(NodePtr x) {
		NodePtr s;
		while (x != root && x->color == 0) {
			if (x == x->parent->left) {
				s = x->parent->right;  // s is right child of x
				if (s->color == 1) {  // if x�s sibling S is red
					s->color = 0;
					x->parent->color = 1;
					left_rotate(x->parent);
					s = x->parent->right;
				}

				if (s->left->color == 0 && s->right->color == 0) {
					//now  if x�s sibling S is black, and both of S�s children are black.
					s->color = 1;
					x = x->parent;
				} else {
					if (s->right->color == 0) {
						// if x�s sibling S is black, S�s left child is red, and S�s right child is black
						s->left->color = 0;
						s->color = 1;
						rotate_right(s);
						s = x->parent->right;
					}

					// if x�s sibling S is black, and S�s right child is red.
					s->color = x->parent->color;
					x->parent->color = 0;
					s->right->color = 0;
					left_rotate(x->parent);
					x = root;
				}
			} else {
				s = x->parent->left;  // if s is left child of x
				if (s->color == 1) {
					// if x�s sibling S is red
					s->color = 0;
					x->parent->color = 1;
					rotate_right(x->parent);
					s = x->parent->left;
				}

				if (s->right->color == 0 && s->right->color == 0) {
					//now  if x�s sibling S is black, and both of S�s children are black.
					s->color = 1;
					x = x->parent;
				} else {
					if (s->left->color == 0) {
						// if x�s sibling S is black, S�s left child is red, and S�s right child is black.
						s->right->color = 0;
						s->color = 1;
						left_rotate(s);
						s = x->parent->left;
					}

					// if x�s sibling S is black, and S�s right child is red.
					s->color = x->parent->color;
					x->parent->color = 0;
					s->left->color = 0;
					rotate_right(x->parent);
					x = root;
				}
			}
		}
		x->color = 0;
	}


	void rbTransplant(NodePtr u, NodePtr v){
		if (u->parent == nullptr) {
			root = v;
		} else if (u == u->parent->left){
			u->parent->left = v;
		} else {
			u->parent->right = v;
		}
		v->parent = u->parent;
	}

	void deleteNodeHelper(NodePtr node, int key) {
		// find the node containing key
		NodePtr z = TNULL;
		NodePtr x, y;
		while (node != TNULL){
			if (node->data == key) {
				z = node;
			}

			if (node->data <= key) {
				node = node->right;
			} else {
				node = node->left;
			}
		}

		if (z == TNULL) {
			cout<<"Couldn't find key in the tree"<<endl;
			return;
		}else{
            cout << "Node Deleted = "<<key<<endl;
		}

		y = z;
		int y_original_color = y->color;       // saving original color of y
		if (z->left == TNULL) {
			x = z->right;
			rbTransplant(z, z->right);
		} else if (z->right == TNULL) {
			x = z->left;
			rbTransplant(z, z->left);
		} else {
			y = minimum(z->right);
			y_original_color = y->color;
			x = y->right;
			if (y->parent == z) {
				x->parent = y;
			} else {
				rbTransplant(y, y->right);
				y->right = z->right;
				y->right->parent = y;
			}

			rbTransplant(z, y);
			y->left = z->left;
			y->left->parent = y;
			y->color = z->color;
		}
		delete z;
		if (y_original_color == 0){
			delete_update(x);
		}
	}
// Now for insertion , using simple BST insertion operation K as red.
// updateing if the insertion violates the red-black tree properties.
//insert_update function to modify w.r.t RBtrees propeties.
	void insert_update(NodePtr k){
		NodePtr u;
		while (k->parent->color == 1) {
			if (k->parent == k->parent->parent->right) {
				u = k->parent->parent->left;
				//u in terms of node called as uncle
				if (u->color == 1) {     // if uncle is red
					u->color = 0;
					k->parent->color = 0;
					k->parent->parent->color = 1;
					k = k->parent->parent;
				} else {
					if (k == k->parent->left) {
						// P is right child of G and K is left child of P.
						k = k->parent;
						rotate_right(k);
					}
					k->parent->color = 0;
					k->parent->parent->color = 1;
					left_rotate(k->parent->parent);
				}
			} else {
				u = k->parent->parent->right; // uncle

				if (u->color == 1) {
					u->color = 0;
					k->parent->color = 0;
					k->parent->parent->color = 1;
					k = k->parent->parent;
				} else {
					if (k == k->parent->right) {
						//  P is left child of G and K is right child of P.
						k = k->parent;
						left_rotate(k);
					}
					// P is left child of G and K is left child of P.
					k->parent->color = 0;
					k->parent->parent->color = 1;
					rotate_right(k->parent->parent);
				}
			}
			if (k == root) {
				break;
			}
		}
		root->color = 0;
		// If T is empty ,K as root of tree  and root k as black
	}

	void printHelper(NodePtr root, string indent, bool last) {
		// print the tree structure on the screen
	   	if (root != TNULL) {
		   cout<<indent;
		   if (last) {
		      cout<<"R----";
		      indent += "     ";
		   } else {
		      cout<<"L----";
		      indent += "|    ";
		   }

           string sColor = root->color?"RED":"BLACK";
		   cout<<root->data<<"("<<sColor<<")"<<endl;
		   printHelper(root->left, indent, false);
		   printHelper(root->right, indent, true);
		}
		// cout<<root->left->data<<endl;
	}

public:
	RBTree() {
		TNULL = new Node;
		TNULL->color = 0;
		TNULL->left = nullptr;
		TNULL->right = nullptr;
		root = TNULL;
	}

	// Pre-Order traversal
	// Node->Left Subtree->Right Subtree
	void preorder() {
		preOrderHelper(this->root);
	}

	// In-Order traversal
	// Left Subtree -> Node -> Right Subtree
	void inorder() {
		inOrderHelper(this->root);
	}

	// Post-Order traversal
	// Left Subtree -> Right Subtree -> Node
	void postorder() {
		postOrderHelper(this->root);
	}

	// search the tree for the key k
	// and return the corresponding node
	NodePtr searchTree(int k) {
		return searchTreeHelper(this->root, k);
	}

	// find the node with the minimum key
	NodePtr minimum(NodePtr node) {
		while (node->left != TNULL) {
			node = node->left;
		}
		return node;
	}

	// find the node with the maximum key
	NodePtr maximum(NodePtr node) {
		while (node->right != TNULL) {
			node = node->right;
		}
		return node;
	}

	// find the successor of a given node
	NodePtr successor(NodePtr x) {
		// if the right subtree is not null,
		// the successor is the leftmost node in the
		// right subtree
		if (x->right != TNULL) {
			return minimum(x->right);
		}

		// else it is the lowest ancestor of x whose
		// left child is also an ancestor of x.
		NodePtr y = x->parent;
		while (y != TNULL && x == y->right) {
			x = y;
			y = y->parent;
		}
		return y;
	}

	// find the predecessor of a given node
	NodePtr predecessor(NodePtr x) {
		// if the left subtree is not null,
		// the predecessor is the rightmost node in the
		// left subtree
		if (x->left != TNULL) {
			return maximum(x->left);
		}

		NodePtr y = x->parent;
		while (y != TNULL && x == y->left) {
			x = y;
			y = y->parent;
		}

		return y;
	}

	// rotate left at node x
	void left_rotate(NodePtr x) {
		NodePtr y = x->right;
		x->right = y->left;
		if (y->left != TNULL) {
			y->left->parent = x;
		}
		y->parent = x->parent;
		if (x->parent == nullptr) {
			this->root = y;
		} else if (x == x->parent->left) {
			x->parent->left = y;
		} else {
			x->parent->right = y;
		}
		y->left = x;
		x->parent = y;
	}

	// rotate right at node x
	void rotate_right(NodePtr x) {
		NodePtr y = x->left;
		x->left = y->right;
		if (y->right != TNULL) {
			y->right->parent = x;
		}
		y->parent = x->parent;
		if (x->parent == nullptr) {
			this->root = y;
		} else if (x == x->parent->right) {
			x->parent->right = y;
		} else {
			x->parent->left = y;
		}
		y->right = x;
		x->parent = y;
	}

	// insert the key to the tree in its appropriate position
	// and update the tree
	void insert(int key) {
		// applying binary search insertion
		NodePtr node = new Node;
		node->parent = nullptr;
		node->data = key;
		node->left = TNULL;
		node->right = TNULL;
		node->color = 1; // new node must be red

		NodePtr y = nullptr;
		NodePtr x = this->root;

		while (x != TNULL) {
			y = x;
			if (node->data < x->data) {
				x = x->left;
			} else {
				x = x->right;
			}
		}

		// y is parent of x
		node->parent = y;
		if (y == nullptr) {
			root = node;
		} else if (node->data < y->data) {
			y->left = node;
		} else {
			y->right = node;
		}

		// if new node is a root node, simply return
		if (node->parent == nullptr){
			node->color = 0;
			return;
		}

		// if the grandparent is null, simply return
		if (node->parent->parent == nullptr) {
			return;
		}

		// update the tree
		insert_update(node);
	}

	NodePtr getRoot(){
		return this->root;
	}

	// delete the node from the tree
	void deleteNode(int data) {
		deleteNodeHelper(this->root, data);
	}

	// print the tree structure on the screen
	void display_data() {
	    if (root) {
            cout << "\n Display"<<endl;
    		printHelper(this->root, "", true);
	    }
	}
};

/// as told position 1 to be considered as index 0 of an array for search, insertion and deletion operation
int main()
{   int ch,length_,y=0;
	int start_, end_;
	int sum_ = 0;
	int count_ =0;
    RBTree bst;
    cout<< "Define length of array = ";
    cin >> length_;
    int n, i, a[length_];
    do
    {
      cout<<"\nRED BLACK TREE ";
                cout<<"\n 1. Insert elements in the tree at index i";
                cout<<"\n 2. Delete a node from the tree from index ";
                cout<<"\n 3. Search for an element in the tree from index";
				cout<<"\n 4. Display the tree ";
                cout<<"\n 5. Ques 1b. To compute RangeAvg Ques 1b";
                cout<<"\n 6. Exit ";
				cout<<"\nEnter Your Choice: ";
                cin>>ch;
                switch(ch)
                {    //case 2 for deletion
					case 2:  int dd;   // enter pos of the number to be deleted
							cout<<"\nEnter the pos of element to be deleted: ";
							cin >> dd;
							bst.deleteNode(a[dd -1]);
							break;
                    // case 3 for search
					case 3 :
						int ss;   // enter pos of the element
						cout<<"\nEnter the position of the element to be searched: ";
						cin>>ss;
						bst.searchTree(a[ss-1]);
						break;
                    //case 4 print display
					case 4 : bst.display_data();
							break;
                    // case 1 for insertion
					case 1:
							int in;
							int value_;
							// initially array has 0 at every index
							for (int x=0 ; x<length_; x++){
								a[x] = 0;
							}
						    // now updating values in the array taken as input
							cout << "enter position at which you want to insert= ";
							cin >> in;
							cout << "enter the value you want to insert at pos = "<<in <<" = ";
							cin >> value_;     // as told position 1 to be considered as index 0
							a[in-1] = value_;
							bst.insert(a[in-1]);
							break;
					case 5:
					    cout << "Ques 1b Range Avg for array inserted in RBtree"<<endl;
						cout << "enter range of elements (enter position): ";
						cout << "\nstarting position: ";
						cin >> start_;
						cout<< "End position: ";
						cin >> end_;
						for ( int av=start_-1; av<= end_-1; av++)
						{
							cout<< av <<"  "<< a[av] << endl;
							sum_= sum_ + a[av];
							count_++;
							cout << sum_<<endl;
						}
						cout << sum_<< " and "<< count_;
						cout << "Average = "<<sum_/count_<< endl;
						break;

					case 6 : y=1;
                        break;
					default : cout<<"\nEnter a Valid Choice.";
                }
                cout<<endl;

    }while(y!=1);
    return 1;

}

