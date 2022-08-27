%{
    int flag = 0;
%}

%%
"//".* {flag=0;}
"/*".*\n?.*"*/" {flag=0;}
"/*".*\n?.* {++flag;}
.*"*/" {--flag;}
. {if(flag == 0) {fprintf(yyout, yytext);}}
%%

int main(int argc, char **argv)
{
    yyin = fopen(argv[1], "r");
    yyout = fopen(argv[2], "w");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
