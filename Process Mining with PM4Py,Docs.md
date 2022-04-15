![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.001.png)

**Process Mining with PM4Py**

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.002.jpeg)

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.003.jpeg)

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.004.jpeg)

1. ***Randy takes your order***
1. ***Randy notes down your preferred payment method***
1. ***Randy notes down your address***
1. ***Luigi prepares your burger***
1. ***Luigi puts your burger in a box***
1. ***Randy wraps your order***
1. ***John delivers your order***

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.005.png)

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.006.png)

Figure 2: Fundamental elements of the ["Business Process Model and Notation"](http://bpmn.org/), i.e., BPMN, notation, taken from [Process Mining: Data Science in Action; Wil M.P. van der Aalst (2016)](https://www.springer.com/gp/book/9783662498507), page 69

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.007.jpeg)

Figure 3: Running example BPMN-based process model describing the behavior of the simple process that we use in this tutorial.

**Install PM4Py**

[**"RuntimeError: Make sure the Graphviz executables are on your system's path" after installing Graphviz 2.38**](https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft)![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.008.png)

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.009.jpeg)

Stack users advice for installation error

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.010.jpeg)

My advice for installation

**Loading CSV Files**



|event\_log =|
| - |
|pm4py.format\_dataframe(pd.read\_csv('C:/Users/ALI/Downloads/tamrins/running|
|-example.csv', sep=';'), case\_id='case\_id',|
|activity\_key='activity', timestamp\_key='timestamp')|
|Csv loading|
**Loading XES Files**

log = pm4py.read\_xes('C:/Users/ALI/Downloads/tamrins/running-example.xes') XES loading![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.011.png)

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.012.jpeg)

XES example dataset

**Pre-Built Event Log Filters**

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.013.png)

Filter\_start\_activities

oE

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.014.png)

Output as a text

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.015.png)

filter\_variants

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.016.png)

Output as a text

**Obtaining a Process Model**

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.017.png)

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.018.png)

Figure 6: BPMN model discovered based on the running example event data set, using the Inductive Miner implementation of PM4Py.

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.019.png)

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.020.png)

Figure 7: Process Tree model discovered based on the running example event data set, using the Inductive Miner implementation of PM4Py.

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.021.png)

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.022.png)

Figure 8: Process Map (DFG-based) discovered based on the running example event data set.

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.023.png)

Distribution of case duration

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.024.png)

Distribution of events over time

**Alpha Miner**

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.025.png)

**Directly-Follows Graph**

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.026.png)

**Frequency/Performance**

Similar to the Directly-Follows graph

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.027.png)

![](Aspose.Words.536437b3-d701-4b56-9ee3-8772743ea048.028.jpeg)

**Rework (activities)**

The rework statistic permits to identify the activities which have been repeated during the same process execution. This shows the underlying inefficiencies in the process.

{'check ticket': 2, 'decide': 2, 'examine casually': 1, 'reinitiate request': 1}

**Rework (cases)**

We define as rework at the case level the number of events of a case having an activity which has appeared previously in the case.

For example, if a case contains the following activities: A,B,A,B,C,D; the rework is 2 since the events in position 3 and 4 are referring to activities that have already been included previously.

{'1': {'number\_activities': 5, 'rework': 0}, '2': {'number\_activities': 5, 'rework': 0}, '3': {'number\_activities': 9, 'rework': 2}, '4': {'number\_activities': 5, 'rework': 0}, '5': {'number\_activities': 13, 'rework': 7}, '6': {'number\_activities': 5, 'rework': 0}}
