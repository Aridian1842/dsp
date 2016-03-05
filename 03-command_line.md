# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

- `pushd` The pushd command takes your current directory and "pushes" it into a list for later, then it changes to another directory. It's like saying, "Save where I am, then go here."
- `popd` The popd command takes the last directory you pushed and "pops" it off, taking you back there.
- `$|$` The | takes the output from the command on the left, and "pipes" it to the command on the right. In line 1 you see me do that.
- `$<$` The < will take and send the input from the file on the right to the program on the left. You see me do that in line 2. This does not work in PowerShell.
- `$>$` The > takes the output of the command on the left, then writes it
to the file on the right. You see me do that on line 9.
- `$>>$`The >> takes the output of the command on the left, then appends it
to the file on the right.
- `find` (e.g., `find . -name "*.txt" -print`) How "find" works is you write in a kind of sentence: "Hey find, start here (.) then find files named *.txt and print them".
- `cat > somefile.txt` `cat` will read whatever you type and then write it to that file.
- `man` get help on a command
- `env` print environment variables (e.g., PATH)

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  lists directory contents
`ls -a`  doesn't ignore entries starting with .
`ls -l`  uses a long listing format
`ls -lh`  print sizes in human readable format
`ls -lah`  print sizes in human readable format and doesn't ignore entries starting with .
`ls -t`  sorts by modification time, newest first
`ls -Glp`  long listing that doesn't print group names and appends `/` to directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

- `ls -u` Displays files by the file access time.
- `ls -R` Displays subdirectories as well.
- `ls -1` Displays each entry on a line.
- `ls -d` Displays only directories.
- `ls -r` Displays files in reverse order.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` builds and executes command lines from standard input. Here's an example that finds files named core in or below the directory /tmp and deletes them:

`find /tmp -name core -type f -print | xargs /bin/rm -f`
 

