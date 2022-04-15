import pandas
import pm4py
import datetime as dt
import os
#def import_csv(file_path):
 #   event_log = pandas.read_csv(file_path, sep=';')
  #  event_log = pm4py.format_dataframe(event_log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')
    #start_activities = pm4py.get_start_activities(event_log)
   # end_activities = pm4py.get_end_activities(event_log)
    #print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

    #num_events = len(event_log)
   # num_cases = len(event_log.case_id.unique())
    #print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))

 #   process_tree = pm4py.discover_tree_inductive(event_log)
 #   pm4py.view_process_tree(process_tree)

 #   event_log = pm4py.format_dataframe(pandas.read_csv('C:/Users/ALI/Downloads/tamrins/running-example.csv', sep=';'), case_id='case_id',
 #   activity_key='activity', timestamp_key='timestamp')
#    event_log.to_csv('C:/Users/ALI/Downloads/tamrins/running-example-exported.csv')

##    import_csv("C:/Users/ALI/Downloads/tamrins/running-example.csv")



import pandas as pd
event_log = pm4py.format_dataframe(pd.read_csv('C:/Users/ALI/Downloads/tamrins/running-example.csv', sep=';'), case_id='case_id',
activity_key='activity', timestamp_key='timestamp')
#event_log.to_csv('C:/Users/ALI/Downloads/tamrins/running-example-exported.csv')
log = pm4py.read_xes('C:/Users/ALI/Downloads/tamrins/running-example.xes')


# Figure 6: BPMN model discovered based on the running example event data set, using the Inductive Miner implementation of PM4Py.
#process_tree = pm4py.discover_tree_inductive(event_log)
#bpmn_model = pm4py.convert_to_bpmn(process_tree)
#pm4py.view_bpmn(bpmn_model)                                  



#https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft

#Figure 7: Process Tree model discovered based on the running example event data set, using the Inductive Miner implementation of PM4Py.
#process_tree = pm4py.discover_tree_inductive(log)
#pm4py.view_process_tree(process_tree)



#Figure 8: Process Map (DFG-based) discovered based on the running example event data set.

#dfg, start_activities, end_activities = pm4py.discover_dfg(log)
#pm4py.view_dfg(dfg, start_activities, end_activities)


#Figure 9: Process Map (HM-based) discovered based on the running example event data set.
#map = pm4py.discover_heuristics_net(log)
#pm4py.view_heuristics_net(map)




#Pre-Built Event Log Filters
'''
filtered = pm4py.filter_start_activities(log, {'register request'})
#print(list[filtered])
with open('register_request_filtered.txt', 'w') as f:
    for i in filtered :
        f.write(str(i)+'\n')


filtered2 = pm4py.filter_end_activities(log, {'pay compensation'})
print(list[filtered2])

with open('pay_compensation.txt', 'w') as f:
    for i in filtered2 :
        f.write(str(i)+'\n')


filtered3 = pm4py.filter_variants(log, [
    ['register request', 'check ticket', 'examine casually', 'decide', 'pay compensation']])

print(str(filtered3))
with open('filter_variants.txt', 'w') as f:
    for i in filtered3 :
        for j in i :
            f.write(str(j)+'\n')


filtered4 = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31), mode='events')
with open('filter_time_range.txt', 'w') as f:
    for i in filtered4:
        stri = str(i)
        res = stri.ljust(8)
        f.write(res+'\n')

'''

#Rework (cases) and (activities)

import pm4py

log = pm4py.read_xes(os.path.join("tests", "input_data", "C:/Users/ALI/Downloads/tamrins/running-example.xes"))
rework = pm4py.get_rework_cases_per_activity(log)
print(rework)
with open('get_rework_cases_per_activity.txt', 'w') as f:
    f.write(str(rework)+'-')

log = pm4py.read_xes('C:/Users/ALI/Downloads/tamrins/running-example.xes')

from pm4py.statistics.rework.cases.log import get as rework_cases

dictio = rework_cases.apply(log)
print('---------------------------')
print(dictio)
with open('rework_cases.txt', 'w') as f:
    f.write(str(dictio)+'-')



'''
#Distribution of case duration
#Distribution of events over time

import os
from pm4py.objects.log.importer.xes import importer as xes_importer
log_path = os.path.join("tests","input_data",'C:/Users/ALI/Downloads/tamrins/running-example.xes')
log = xes_importer.apply(log_path)

from pm4py.util import constants
from pm4py.statistics.traces.generic.log import case_statistics
x, y = case_statistics.get_kde_caseduration(log, parameters={constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "time:timestamp"})

from pm4py.visualization.graphs import visualizer as graphs_visualizer

gviz = graphs_visualizer.apply_semilogx(x, y, variant=graphs_visualizer.Variants.CASES)
graphs_visualizer.view(gviz)

from pm4py.algo.filtering.log.attributes import attributes_filter

x, y = attributes_filter.get_kde_date_attribute(log, attribute="time:timestamp")

from pm4py.visualization.graphs import visualizer as graphs_visualizer

gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.DATES)
graphs_visualizer.view(gviz)


'''


'''
#Alpha Miner
import os
from pm4py.objects.log.importer.xes import importer as xes_importer

log = xes_importer.apply(os.path.join("tests","input_data","C:/Users/ALI/Downloads/tamrins/running-example.xes"))

from pm4py.algo.discovery.alpha import algorithm as alpha_miner
net, initial_marking, final_marking = alpha_miner.apply(log)

from pm4py.visualization.petri_net import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)

'''


'''
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
log = xes_importer.apply(os.path.join("tests","input_data","C:/Users/ALI/Downloads/tamrins/running-example.xes"))

from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
dfg = dfg_discovery.apply(log)

from pm4py.visualization.dfg import visualizer as dfg_visualization
gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.FREQUENCY)
dfg_visualization.view(gviz)


'''

'''
import os
from pm4py.objects.log.importer.xes import importer as xes_importer

log = xes_importer.apply(os.path.join("tests","input_data","C:/Users/ALI/Downloads/tamrins/running-example.xes"))

from pm4py.algo.discovery.alpha import algorithm as alpha_miner
net, initial_marking, final_marking = alpha_miner.apply(log)
from pm4py.visualization.petri_net import visualizer as pn_visualizer
parameters = {pn_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
gviz = pn_visualizer.apply(net, initial_marking, final_marking, parameters=parameters, variant=pn_visualizer.Variants.FREQUENCY, log=log)
pn_visualizer.save(gviz, "inductive_frequency.png")   
                     
'''
                         
