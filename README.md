# devsecops-coding-test

In this exercise you can use any language of your choice, except shell script. The goal is to implement a function that combines 2 sorted arrays into a single sorted array. The function should be invoked from command line with the 2 sorted arrays as the arguments.
Here are sample inputs and outputs:

```
$ function_name [1, 2, 7, 9] [3, 6, 8]
> [1, 2, 3, 6, 7, 8, 9]

$ function_name [6, 8, 9] [1, 4, 6]
> [1, 4, 6, 6, 8, 9]

$ function_name [] [1, 2, 3]
> [1, 2, 3]
```

The next step is to containerize the function. The end result should look like this:

```
$ docker run <image>:<tag> [1, 2, 7, 9] [3, 6, 8]
> [1, 2, 3, 6, 7, 8, 9]
```

Create a public github repo for this exercise and include all files required to build and run the containerized function. Use a README for build and run steps if necessary. Please submit the github repo within a week of receiving the exercise.
