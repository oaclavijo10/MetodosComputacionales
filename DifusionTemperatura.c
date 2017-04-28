#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float * difusioncaso1C(int i,int j,int t,float suma,float dx,float dy,float v,float dt,int space,int time,float alfa, float beta)
{
  static float r[10000];
  float dif[space+1][space+1];
   /*Condiciones iniciales*/
  for(i=1;i<space;i++){
    for(j=1;j<space;j++){
      dif[i][j]=50;
    }
  }
  for(i=21;i<32;i++){
    for(j=41;j<62;j++){
      dif[i][j]=100;
    }
  }
  /*Calculo*/
  for(t=0;t<time;t++){
    suma=0;
    for(i=1;i<space-2;i++){
      dif[i][0]=50;
      dif[i][space]=50;
      dif[0][i]=50;
      dif[space][i]=50;
      for(j=1;j<space-2;j++){
        if(t==0){
          printf("1, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
        }
        else if(t==400){
          printf("1, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
        }
        else if(t==10000){
          printf("1, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
        }
        dif[i][j]=alfa*(dif[i+1][j]+dif[i-1][j]) + beta*(dif[i][j+1]+dif[i][j-1]) + (1-2*alfa-2*beta)*dif[i][j];
        suma=suma+dif[i][j];	
    
      }      
    }
  r[t]=suma/((space-3)*(space-3));
  }
  return r;
}  

float * difusioncaso1P(int i,int j,int t,float suma,float dx,float dy,float v,float dt,int space,int time,float alfa, float beta)
{
  static float r[10000];
  float dif[space+1][space+1];
   /*Condiciones iniciales*/
  for(i=1;i<space;i++){
    for(j=1;j<space;j++){
      dif[i][j]=50;
    }
  }
  for(i=21;i<32;i++){
    for(j=41;j<62;j++){
      dif[i][j]=100;
    }
  }
  /*Calculo*/
  for(t=0;t<time;t++){
    suma=0;
    for(i=1;i<space-2;i++){
      dif[i][0]=dif[i][space-1];
      dif[i][space]=dif[i][1];
      dif[0][i]=dif[space-1][i];
      dif[space][i]=dif[1][i];
      for(j=1;j<space-2;j++){
    if(t==0){
      printf("2, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    else if(t==400){
      printf("2, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    else if(t==10000){
      printf("2, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    dif[i][j]=alfa*(dif[i+1][j]+dif[i-1][j]) + beta*(dif[i][j+1]+dif[i][j-1]) + (1-2*alfa-2*beta)*dif[i][j];
    suma=suma+dif[i][j];
      }      
    }
  r[t]=suma/((space-3)*(space-3));
  }
  return r;
}

float * difusioncaso1A(int i,int j,int t,float suma,float dx,float dy,float v,float dt,int space,int time,float alfa, float beta)
{
  static float r[10000];
  float dif[space+1][space+1];
   /*Condiciones iniciales*/
  for(i=1;i<space;i++){
    for(j=1;j<space;j++){
      dif[i][j]=50;
    }
  }
  for(i=21;i<32;i++){
    for(j=41;j<62;j++){
      dif[i][j]=100;
    }
  }
  /*Calculo*/
  for(t=0;t<time;t++){
  suma=0;
    for(i=1;i<space-2;i++){
      dif[i][0]=dif[i][1];
      dif[i][space]=dif[i][space-1];
      dif[0][i]=dif[1][i];
      dif[space][i]=dif[space-1][i];
      for(j=1;j<space-2;j++){
    if(t==0){
      printf("3, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    else if(t==400){
      printf("3, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    else if(t==10000){
      printf("3, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    dif[i][j]=alfa*(dif[i+1][j]+dif[i-1][j]) + beta*(dif[i][j+1]+dif[i][j-1]) + (1-2*alfa-2*beta)*dif[i][j];
    suma=suma+dif[i][j];
      }      
    }
  r[t]=suma/((space-3)*(space-3));
  }
  return r;
}

float * difusioncaso2C(int i,int j,int t,float suma,float dx,float dy,float v,float dt,int space,int time,float alfa, float beta)
{
  static float r[10000];
  float dif[space+1][space+1];
   /*Condiciones iniciales*/
  for(i=1;i<space;i++){
    for(j=1;j<space;j++){
      dif[i][j]=50;
    }
  }
  for(i=21;i<32;i++){
    for(j=41;j<62;j++){
      dif[i][j]=100;
    }
  }
  /*Calculo*/
  for(t=0;t<time;t++){
  suma=0;
    for(i=21;i<32;i++){
      for(j=41;j<62;j++){
    dif[i][j]=100;
      }
    }
    for(i=1;i<space-2;i++){
      dif[i][0]=50;
      dif[i][space]=50;
      dif[0][i]=50;
      dif[space][i]=50;
      for(j=1;j<space-2;j++){
    if(t==0){
      printf("4, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    else if(t==400){
      printf("4, %d ,%d ,%d, %f\n",t,i,j,dif[i][j] );
    }
    else if(t==10000){
      printf("4, %d ,%d ,%d, %f\n",t,i,j,dif[i][j] );
    }
    dif[i][j]=alfa*(dif[i+1][j]+dif[i-1][j]) + beta*(dif[i][j+1]+dif[i][j-1]) + (1-2*alfa-2*beta)*dif[i][j];
    suma=suma+dif[i][j];
      }      
    }
  r[t]=suma/((space-3)*(space-3));
  }
  return r;
}  

float * difusioncaso2P(int i,int j,int t,float suma,float dx,float dy,float v,float dt,int space,int time,float alfa, float beta)
{
  static float r[10000];
  float dif[space+1][space+1];
   /*Condiciones iniciales*/
  for(i=1;i<space;i++){
    for(j=1;j<space;j++){
      dif[i][j]=50;
    }
  }
  for(i=21;i<32;i++){
    for(j=41;j<62;j++){
      dif[i][j]=100;
    }
  }
  /*Calculo*/
  for(t=0;t<time;t++){
  suma=0;
    for(i=21;i<32;i++){
      for(j=41;j<62;j++){
    dif[i][j]=100;
      }
    }
    for(i=1;i<space-2;i++){
      dif[i][0]=dif[i][space-1];
      dif[i][space]=dif[i][1];
      dif[0][i]=dif[space-1][i];
      dif[space][i]=dif[1][i];
      for(j=1;j<space-2;j++){
    if(t==0){
      printf("5, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    else if(t==400){
      printf("5, %d ,%d ,%d, %f\n",t,i,j,dif[i][j] );
    }
    else if(t==10000){
      printf("5, %d ,%d ,%d, %f\n",t,i,j,dif[i][j] );
    }
    dif[i][j]=alfa*(dif[i+1][j]+dif[i-1][j]) + beta*(dif[i][j+1]+dif[i][j-1]) + (1-2*alfa-2*beta)*dif[i][j];
    suma=suma+dif[i][j];
      }      
    }
  r[t]=suma/((space-3)*(space-3));
  }
  return r;
}

float * difusioncaso2A(int i,int j,int t,float suma,float dx,float dy,float v,float dt,int space,int time,float alfa, float beta)
{
  static float r[10000];
  float dif[space+1][space+1];
   /*Condiciones iniciales*/
  for(i=1;i<space;i++){
    for(j=1;j<space;j++){
      dif[i][j]=50;
    }
  }
  for(i=21;i<32;i++){
    for(j=41;j<62;j++){
      dif[i][j]=100;
    }
  }
  /*Calculo*/
  for(t=0;t<time;t++){
  suma=0;
    for(i=21;i<32;i++){
      for(j=41;j<62;j++){
    dif[i][j]=100;
      }
    }
    for(i=1;i<space-2;i++){
      dif[i][0]=dif[i][1];
      dif[i][space]=dif[i][space-1];
      dif[0][i]=dif[1][i];
      dif[space][i]=dif[space-1][i];
      for(j=1;j<space-2;j++){
    if(t==0){
      printf("6, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    else if(t==400){
      printf("6, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    else if(t==10000){
      printf("6, %d ,%d ,%d, %f\n",t,i,j, dif[i][j] );
    }
    dif[i][j]=alfa*(dif[i+1][j]+dif[i-1][j]) + beta*(dif[i][j+1]+dif[i][j-1]) + (1-2*alfa-2*beta)*dif[i][j];
    suma=suma+dif[i][j];
      }      
    }
  r[t]=suma/((space-3)*(space-3));
  }
  return r;
}

int main(){
  int i;
  int j;
  int t;
  int l;
  float *p1C;
  float *p1P;
  float *p1A;
  float *p2C;
  float *p2P;
  float *p2A;
  float suma=0;
  float dx=0.01;
  float dy=0.01;
  float v=0.0001;
  float dt=(dx*dy)/(4*v);
  int space=100; /*1/dx*/
  int time=10001; /*2500/dt*/
  float alfa=(v*dt)/(dx*dx);
  float beta=(v*dt)/(dy*dy);
  p1C=difusioncaso1C(i,j,t,suma,dx,dy,v,dt,space,time,alfa,beta);
  p1P=difusioncaso1P(i,j,t,suma,dx,dy,v,dt,space,time,alfa,beta);
  p1A=difusioncaso1A(i,j,t,suma,dx,dy,v,dt,space,time,alfa,beta);
  p2C=difusioncaso2C(i,j,t,suma,dx,dy,v,dt,space,time,alfa,beta);
  p2P=difusioncaso2P(i,j,t,suma,dx,dy,v,dt,space,time,alfa,beta);
  p2A=difusioncaso2A(i,j,t,suma,dx,dy,v,dt,space,time,alfa,beta);
  for(i=0;i<10000;i++){
    printf("%d, %f , %d , %d , %d\n", 1,p1C[i],0,0,0);
  }
  for(i=0;i<10000;i++){
    printf("%d, %f , %d , %d , %d\n", 2,p1P[i],0,0,0);
  }
  for(i=0;i<10000;i++){
    printf("%d, %f , %d , %d , %d\n", 3,p1A[i],0,0,0);
  }
  for(i=0;i<10000;i++){
    printf("%d, %f , %d , %d , %d\n", 4,p2C[i],0,0,0);
  }
  for(i=0;i<10000;i++){
    printf("%d, %f , %d , %d , %d\n", 5,p2P[i],0,0,0);
  }
  for(i=0;i<10000;i++){
    printf("%d, %f , %d , %d , %d\n", 6,p2A[i],0,0,0);
  }
  return 0;
}
