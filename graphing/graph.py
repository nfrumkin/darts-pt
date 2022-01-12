import matplotlib.pyplot as plt
import numpy as np
f = open("proj_full_stats.txt", 'r')

# iter = 0
# proj_types = []
# accuracies = []
# proj_ids = []
# latencies = []
# for line in f.readlines():
#     line = line.split(" ")
#     if line[0] in ['begin', 'end']:
#         # print(line)
#         if len(proj_types) != 0:
#             iter += 1
#             num_edges = int(len(proj_types)/2)
#             fig, (ax1, ax2) = plt.subplots(2)
#             fig.suptitle("Projection Step #"+str(iter))
#             for i in range(0, num_edges):
#                 ax1.plot([float(latencies[i])], [float(accuracies[i])], "*", label=proj_types[i]+proj_ids[i])
#                 ax1.set_title("Normal Cell")
#             for i in range(num_edges, len(proj_types)):
#                 ax2.plot(float(latencies[i]), float(accuracies[i]), "*", label=proj_types[i]+proj_ids[i])
#                 ax2.set_title("Reduction Cell")
#                 ax2.set_xlabel("latency")
#                 ax2.set_ylabel("accurcy")
#             # ax2.legend()
#             plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#             fig.tight_layout()
#             plt.savefig("graphs/"+"iteration"+str(iter)+".png")   
#             plt.close()
#         proj_types = []
#         accuracies = []
#         proj_ids = []
#         latencies = []
#     else:
#         proj_type = line[0]
#         proj_id = line[1]
#         accuracy = line[2]
#         latency = line[4]
#         proj_types.append(proj_type)
#         proj_ids.append(proj_id)
#         accuracies.append(accuracy)
#         latencies.append(latency)

# iter = 0
# accuracies = []
# latencies = []
# for line in f.readlines():
#     line = line.split(" ")
#     if line[0] in ['begin', 'end']:
#         # print(line)
#         proj_type = line[0]
#         proj_id = line[1]
#         accuracy = line[2]
#         latency = line[4]
#         accuracies.append(float(accuracy))
#         latencies.append(float(latency))
#     elif len(accuracies) != 0:
#         plt.plot(latencies, accuracies, "*", label=str(iter))
#         mean_latency = np.mean(latencies)
#         sigma_latency = np.std(latencies)
#         mean_accuracy = np.mean(accuracies)
#         sigma_accuracy = np.var(accuracies)
#         # print(mean_accuracy)
#         # print(sigma_accuracy)
#         print(mean_latency)
#         # print(sigma_latency)
#         iter += 1
#         accuracies = []
#         latencies = []
            
        

# plt.title("Supernet as Projection continues")
# plt.xlabel("latency")
# plt.ylabel("accurcy")
# # plt.legend()
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# plt.tight_layout()
# plt.savefig("graphs/normal_samples.png")   
# plt.close()


iter = 0
proj_types = []
accuracies = []
proj_ids = []
latencies = []
for line in f.readlines():
    line = line.split(" ")
    if line[0] in ['begin', 'end']:
        # print(line)
        if len(proj_types) != 0:
            iter += 1
            num_edges = int(len(proj_types)/2)
            mean_accuracy = np.mean(accuracies[num_edges:])
            print(mean_accuracy)
            # mean_latency = np.mean(latencies[num_edges:])
            # print(mean_latency)
            # std_latency = np.std(latencies[num_edges:])
            # print(std_latency)
        proj_types = []
        accuracies = []
        proj_ids = []
        latencies = []
    else:
        proj_type = line[0]
        proj_id = line[1]
        accuracy = line[2]
        latency = line[4]
        proj_types.append(proj_type)
        proj_ids.append(proj_id)
        accuracies.append(float(accuracy))
        latencies.append(float(latency))