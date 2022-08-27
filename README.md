## Diff Checker Code Comments

### Introduction

This repository contains the scripts to remove comments - single line and 
multi-line comments written in the [javadoc](https://www.oracle.com/in/technical-resources/articles/java/javadoc-tool.html#:~:text=The%20special%20comments%20in%20the,to%20generate%20the%20API%20docs.&text=The%20JDK%20tool%20that%20generates%20API%20documentation%20from%20documentation%20comments.) style 

Javadoc comments are written in the following format:

```
    /**
    * Returns an Image object that can then be painted on the screen. 
    * The url argument must specify an absolute <a href="#{@link}">{@link URL}</a>. The name
    * argument is a specifier that is relative to the url argument. 
    * <p>
    * This method always returns immediately, whether or not the 
    * image exists. When this applet attempts to draw the image on
    * the screen, the data will be loaded. The graphics primitives 
    * that draw the image will incrementally paint on the screen. 
    *
    * @param  url  an absolute URL giving the base location of the image
    * @param  name the location of the image, relative to the url argument
    * @return      the image at the specified URL
    * @see         Image
    */

    public Image getImage(URL url, String name) {
        try {
            return getImage(new URL(url, name));
        } catch (MalformedURLException e) {
            return null;
        }
    }
```

This style is used to write API documentation 

### Use case
During the course of my GSoD project, I have been writing API documentation for C/C++ code using the documentation generator Doxygen

To avoid the possibility that the source code may be modified in the process of doing so, I 
created a script written in `lex` that can be used to remove comments from the source code.
A diff of the 2 files can be performed to ensure the integrity of the source code 

### Usage 

1. Install `lex`/`flex`. Lex is the lexical analyser that parses the input source code and tokenises it 

2. Execute `lex remove_comments.l`. This produces a file `lex.yy.c`. 
Read more about what a lexical analyser does [here](https://blog.devgenius.io/a-simple-lexical-analyser-aaa4329b18d0) 

3. Execute `cc lex.yy.c`, this generates the executable `a.out`, like any other C program 

4. Run `./a.out <source-file> <target-file>`, where `<source file>` is the file with comments and `<target file>` is a new file without comments


### Example 

1. Consider a sample file `input.cpp` with the contents  

```

/** 
 * This is a sample input which javadoc style comments 
 */
#include<stdio.h>

int main(){
	/**
	 * Performs the addition of 3 and 5
	 */
	printf("The sum of 3 and 5 is %d\n", 3+5);
	return 0;
}


```


2. On executing the above-mentioned commands, the output is in file `output.cpp`

```



#include<stdio.h>

int main(){
	

	printf("The sum of 3 and 5 is d\n", 3+5);
	return 0;
}



```

The output has newlines which can be removed during further preprocessing