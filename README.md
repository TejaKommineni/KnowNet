# KnowNet

This Repo consists of my thesis work. I am still working on it. Here is it's abstract.

Network administrators perform various activities every day in order to keep an organizations
network healthy. Networks are complex and hence admins take the assistance
of different tools to maintain these networks. The tools used by admins perform aggregation
at different levels for performance management, security, maintaining the quality
of service and others. Aggregating at port level to understand the behavior of flows is
well studied whereas understanding the behavior of hosts and groups of hosts is less well
studied. The latter is helpful to admins in making informed decisions regarding activities
that include security policies and capacity planning among many others. Looking at flow
level doesnt help us in understanding the total activities each host is undertaking and
doesnt figure out which hosts are behaving alike as flow is just an instance of communication
between two hosts. Hence, we want to aggregate by hosts and group them by
understanding their behaviour.
As we have millions of flows and thousands of hosts to work on, we used data mining
techniques to find the structure and present them to admins to help them make decisions
and ease enterprise network management.
We have built a system that consumes flow records of network as input and determines
the host behaviors in the network and groups the hosts accordingly. We also built an
accompanying tool to this system that analyzes the host behaviors in different dimensions.
This approach of extracting behaviors from network data has helped us in gaining
interesting insights into the users of the system. We claim that analyzing host behaviors
can help in uncovering the vulnerabilities in network security that are not found through
traditional tools. We also claim that hosts behaving similarly require similar amount of
network resources and this will be an efficient way for network admins to plan their
network capacity compared to the present bandwidth monitoring techniques.
