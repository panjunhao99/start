#include <math.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>


int main() {
	int tape_len = 101;
	int input_len = 11;
	int scan_start = tape_len - input_len;//扫描开始=敲入长度-输入长度=90 
	int x,y;
	int state = 0;//状态开始为0 
	
	char infi_tape[tape_len];//初始 
	char input[input_len];
	char *scan;//扫描指针 
	
	do{
		printf("该程序用于展示f(x,y)=x^y的图灵机，带长有限，输入数据之和不要大于999，,计算结果不要大于2048\n");
		printf("请输入x：");

		
		scanf("%d", &x); 
		printf("请输入y：");
		scanf("%d", &y); 
		
	}while( (x+y)>999 || x<0 || y<0);

	for(int i=0; i<input_len; i++){
		input[i] = ' ';//初始化输入数组 
	}
	
	input[0] = '1';
	for(int i=0; i<x; i++){
		input[i+2] = '1'; 
	}
	for(int i=0; i<y; i++){
		input[i+x+3] = '1';
	}
	printf("输入带（第一个1为设定的格式）：\n%s\n", input);
	system("pause");
	for(int i=0; i<tape_len; i++){
		infi_tape[i] = ' ';//初始全为空 
	}
	
	for(int i=0; input[i]!='\0'; i++){
		infi_tape[scan_start+i] = input[i];
	
	}
	
	scan = infi_tape + scan_start;
	while(1){
		if(state==0&&*scan=='1'){state = 0;*scan = 'z';scan++;}//当状态为0，扫描到的值为1，状态依旧为0，指针指向置为z，指针前进加一 
		else if(state==0&&*scan==' '){state = 1;*scan = ' ';scan++;}//当状态为0，扫描到的值为空，状态置为1，指针指向置为空，指针前进加一 
		else if(state==1&&*scan=='1'){state = 1;*scan = 'x';scan++;}//当状态为1，扫描到的值为1，状态置为1，指针指向置为x，指针+1 
		else if(state==1&&*scan==' '){state = 2;*scan = ' ';scan++;}//
		else if(state==2&&*scan=='1'){state = 2;*scan = 'y';scan++;}//
		else if(state==2&&*scan==' '){state = 3;*scan = ' ';scan--;}//
		else if(state==3&&*scan=='y'){state = 3;*scan = 'y';scan--;}//
		else if(state==3&&*scan==' '){state = 3;*scan = ' ';scan--;}//
		else if(state==3&&*scan=='x'){state = 3;*scan = 'x';scan--;}//
		else if(state==3&&*scan=='z'){state = 23;*scan = 'z';scan++;}//
		else if(state==23&&*scan==' '){state = 24;*scan = ' ';scan++;}//
		else if(state==24&&*scan=='x'){state = 24;*scan = 'x';scan++;}//
		else if(state==24&&*scan==' '){state = 4;*scan = ' ';scan++;}//
		else if(state==4&&*scan=='0'){state = 4;*scan = '0';scan++;}//
		else if(state==4&&*scan=='y'){state = 5;*scan = '0';scan--;}//
		else if(state==5&&*scan==' '){state = 5;*scan = ' ';scan--;}//
		else if(state==5&&*scan=='0'){state = 5;*scan = '0';scan--;}//
		else if(state==5&&*scan=='x'){state = 5;*scan = 'x';scan--;}//
		else if(state==5&&*scan=='z'){state = 6;*scan = 'z';scan++;}//
		else if(state==6&&*scan==' '){state = 7;*scan = ' ';scan++;}//
		else if(state==7&&*scan=='x'){state = 8;*scan = '0';scan--;}//
		else if(state==8&&*scan=='0'){state = 8;*scan = '0';scan--;}//
		else if(state==7&&*scan=='0'){state = 7;*scan = '0';scan++;}//
		else if(state==8&&*scan==' '){state = 8;*scan = ' ';scan--;}//
		else if(state==8&&*scan=='z'){state = 9;*scan = 'z';scan--;}//
		else if(state==9&&*scan=='z'){state = 9;*scan = 'z';scan--;}//
		else if(state==9&&*scan=='1'){state = 9;*scan = '1';scan--;}//
		else if(state==9&&*scan==' '){state = 10;*scan = ' ';scan++;}//
		else if(state==10&&*scan=='0'){state = 10;*scan = '0';scan++;}//
		else if(state==10&&*scan=='1'){state = 10;*scan = '1';scan++;}//
		else if(state==10&&*scan=='z'){state = 11;*scan = '0';scan--;}//
		else if(state==11&&*scan=='0'){state = 11;*scan = '0';scan--;}//
		else if(state==11&&*scan=='1'){state = 11;*scan = '1';scan--;}//
		else if(state==11&&*scan==' '){state = 10;*scan = '1';scan++;}//
		else if(state==10&&*scan==' '){state = 12;*scan = ' ';scan--;}//
		else if(state==12&&*scan=='0'){state = 12;*scan = '0';scan--;}//
		else if(state==12&&*scan=='1'){state = 13;*scan = '1';scan++;}//
		else if(state==13&&*scan=='0'){state = 13;*scan = 'z';scan++;}//
		else if(state==13&&*scan==' '){state = 7;*scan = ' ';scan++;}//
		else if(state==7&&*scan==' '){state = 14;*scan = ' ';scan--;}//
		else if(state==14&&*scan=='0'){state = 14;*scan = '0';scan--;}//
		else if(state==14&&*scan==' '){state = 15;*scan = ' ';scan--;}//
		else if(state==15&&*scan=='z'){state = 15;*scan = 'z';scan--;}//
		else if(state==15&&*scan=='1'){state = 15;*scan = '1';scan--;}//
		else if(state==15&&*scan==' '){state = 16;*scan = ' ';scan++;}//
		else if(state==16&&*scan=='1'){state = 16;*scan = '1';scan++;}//
		else if(state==16&&*scan=='z'){state = 17;*scan = '0';scan--;}//
		else if(state==16&&*scan=='0'){state = 16;*scan = '0';scan++;}//
		else if(state==17&&*scan=='1'){state = 17;*scan = '1';scan--;}//
		else if(state==17&&*scan=='0'){state = 17;*scan = '0';scan--;}//
		else if(state==17&&*scan==' '){state = 18;*scan = ' ';scan++;}//
		else if(state==18&&*scan=='1'){state = 16;*scan = ' ';scan++;}//
		else if(state==16&&*scan==' '){state = 20;*scan = ' ';scan--;}//
		else if(state==20&&*scan=='0'){state = 20;*scan = 'z';scan--;}//
		else if(state==20&&*scan=='1'){state = 20;*scan = 'z';scan--;}//
		else if(state==20&&*scan==' '){state = 21;*scan = ' ';scan++;}//
		else if(state==21&&*scan=='z'){state = 21;*scan = 'z';scan++;}//
		else if(state==21&&*scan==' '){state = 22;*scan = ' ';scan++;}//
		else if(state==22&&*scan=='0'){state = 22;*scan = 'x';scan++;}//
		else if(state==22&&*scan==' '){state = 4;*scan = ' ';scan++;}//
		else if(state==4&&*scan==' '){state = 25;*scan = ' ';scan--;}//
		else if(state==25&&*scan=='0'){state = 25;*scan = '1';scan--;}//
		else if(state==25&&*scan==' '){state = 26;*scan = ' ';scan--;}//
		else if(state==26&&*scan=='x'){state = 26;*scan = '1';scan--;}//
		else if(state==26&&*scan==' '){state = 27;*scan = ' ';scan--;}//
		else if(state==27&&*scan=='z'){state = 27;*scan = '1';scan--;}//
		else if(state==27&&*scan==' '){break;}
		printf("%s,state=%d,scan=%d\n", infi_tape, state, (scan-infi_tape));
	}
	
	// print entire tape
	printf("最后的带状态为：\n%s\n", infi_tape);
	int res = 0; 
	for(int i=0; i<tape_len; i++){
		int j = 0;
		for(; infi_tape[j]==' ';j++){}
		for(; infi_tape[j]=='1';j++){
			res++;
		}
		if(infi_tape[j]==' '){
			break;
		}
	}
	printf("计算结果为：%d\n", res);
	system("pause");
	return 0;
}
