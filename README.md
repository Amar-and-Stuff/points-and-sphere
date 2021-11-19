
//polynomial addition
//polynomial
#include<stdio.h>
#include<stdlib.h>
char ch='y';
typedef struct slist
{
 int coff;
 int exp;
 struct slist *link;
}node;
void create(node **p);
void disp(node *p);
void add(node *p, node *q, node **r);
void create(node **p)
{ node *k;
printf("Enter the first term of equation\n");
do
{
 node *t;
 t= malloc(sizeof(node));
 printf("enter the coefficent...");
 scanf("%d",&t->coff);
 printf("enterthe exponent...");
 scanf("%d",&t->exp);
 if(*p==NULL)
 { *p=t;k=t;}
 else
 { k->link=t;k=t;}
 printf("do U want to enter the next term of the equation(y/n)..");
 scanf(" %c",&ch);
}while(ch=='y');
k->link=NULL;
}
void disp(node *p)
{ node *t = p;
if(p==NULL)
{
 printf("The expression is empty");
 return;
}
while(t!=NULL)
{
 printf("%dX^%d ",t->coff,t->exp);
 t=t->link;
 if(t!=NULL) printf("+ ");
}
printf("\n");
}
void add(node *p, node *q, node **r)
{
node *i=p,*j=q,*k=NULL,*temp;
while(i!=NULL&&j!=NULL)
{
 temp= malloc(sizeof(node));
 if(i->exp==j->exp)
 {
 temp->coff=i->coff+j->coff;
 temp->exp=i->exp;
 i=i->link;
 j=j->link;
 }
 else if(i->exp>j->exp)
 {
 temp->coff=i->coff;
 temp->exp=i->exp;
 i=i->link;
 }
 else
 {
 temp->coff=j->coff;
 temp->exp=j->exp;
 j=j->link;
 }
 if(*r==NULL)
 {
 *r=k=temp;
 }
 else
 {
 k->link=temp;
 k=temp;
 }
}
if(i==NULL)
 while(j!=NULL)
 {
 temp= malloc(sizeof(node));
 temp->coff=j->coff;
 temp->exp=j->exp;
 k->link=temp;
 k=temp;
 j=j->link;
 }
else
 while(i!=NULL)
 {
 temp= malloc(sizeof(node));
 temp->coff=i->coff;
 temp->exp=i->exp;
k->link=temp;
 k=temp;
 i=i->link;
 }
k->link=NULL;
}
void main()
{
node *f=NULL, *s=NULL,*r=NULL;
clrscr();
printf("Enter the First Polynomial Equation\n");
create(&f);
printf("Enter the Second Polynomial Equation\n");
create(&s);
clrscr();
printf(" The Given First Polynomial Equation is ..\n");
disp(f);
printf(" The Given Second Polynomial Equation is ..\n");
disp(s);
add(f,s,&r);
printf(" The Resultant Polynomial Equation is ..\n");
disp(r);
}








//Evaluation of Postfix expression 
#include<stdio.h> 
#include<math.h> 
char ch='y'; 
int top=-1; 
float stk[50]; 
void push(float p) 
{ 
 stk[++top]=p; 
} 
float pop() 
{ 
 return stk[top--]; 
} 
void main() 
 { 
 char p[50]; 
 float data[50],a,b; 
 int i,n; 
 while(ch=='y'||ch=='Y') 
 { 
 clrscr(); 
 printf("Enter Postfix Expression with out any blank spaces:"); 
 scanf("%s",p); 
 n=0; 
 while(p[n]!='\0') 
 { 
 if(isalpha(p[n])) 
 { 
 printf("Enter values of %c:",p[n]); 
 scanf("%f",&data[n]); 
 } 
 n++; 
 } 
 p[n]=')'; 
 i=0; 
 while(p[i]!=')') 
 { 
 switch(p[i]) 
 { 
 case'+':a=pop();b=pop();push(b+a);break; 
 case'-':a=pop();b=pop();push(b-a);break; 
 case'*':a=pop();b=pop();push(b*a);break; 
 case'/':a=pop();b=pop();push(b/a);break; 
 case'^':a=pop();b=pop();push(pow(b,a));break; 
 default:push(data[i]); 
 } 
 i++; 
 } 
 printf("The given postfix expression is:"); 
 for(i=0;i<n;i++) 
 { 
 if(isalpha(p[i])) 
 printf("%f ",data[i]);
else 
 printf("%c ",p[i]); 
 } 
 printf("\nThe result of evaluated postfix expression is:%f",pop()); 
 printf("Do you want evaluate another expression: (y/n)"); 
 ch=getchar(); 
 } 
}







//Graph Traversal-BFS 
#include <stdio.h> 
int f=-1,r=-1,q[25]; 
void ins(int v); 
int del(); 
void ins(int n) 
{ 
 if(r==-1) 
 f=r=0; 
 else 
 r++; 
 q[r]=n; 
} 
int del() 
{ 
 if(f==-1) return(-1); 
 else 
 { 
 int t=q[f]; 
 if(f==r) 
 f=r=-1; 
 else f++; 
 return t; 
 } 
} 
void main() 
{ 
 int cost[25][25],nv,v,ne,visit[25],i,j,k,flag=1; 
 printf("Enter the number of vertices..."); 
 scanf("%d",&nv); 
 //initialize the cost matrix 
 for(i=1;i<=nv;i++) 
 for(j=1;j<=nv;j++) 
 cost[i][j]=0; 
 for(i=1;i<=nv;i++) 
 visit[i]=0; 
 printf("enter the number of edges..."); 
 scanf("%d",&ne); 
 printf(" Enter the edges(i,j).../n"); 
 for(k=1;k<=ne;k++) 
 { 
 scanf("%d %d",&i,&j); 
 cost[i][j]=1; 
 } 
 printf("enter the source vertex.."); 
 scanf("%d",&v); 
 printf("According BFS, the visiting sequence of the vertices are.../n"); 
 printf("%d ",v); 
 visit[v]=1; 
 while(flag==1) 
 { 
 for(j=1;j<=nv;j++) 
 { 
 if(cost[v][j]!=0 && visit[j]==0)
{ 
 visit[j]=1; 
 printf("%d ",j); 
 ins(j); 
 } 
 } 
 v=del(); 
 if(v==-1) flag=0; 
 } 
}
