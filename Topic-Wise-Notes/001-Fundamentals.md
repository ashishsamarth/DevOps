**Devops-Fundamentals**
--------------------------------------------------------------------------------------------------------------------------
Dev-OPS Core Values :

    - Culture
    - Automation
    - Measurement
    - Sharing

a. What is Culture
--------------------------------------------------------------------------------------------------------------------------
Earlier, teams in IT were split across 'Development' and 'Operations' with their focus split across 'Develop the Functionality' vs 'Maintainence of the system'. They often did not speak the same languauge in terms of day to day operations, and had different understanding.

b. What is Automation
--------------------------------------------------------------------------------------------------------------------------
The idea is to bring balance in to system in terms of People > Process > Tools and then evaluate if whatever you plan to automate reflects in to business values.

c. What is Measurement
--------------------------------------------------------------------------------------------------------------------------
Its the metrics for evaluation of what is being done and it can be in multiple classifications
MTTR, Cycle Time, Costs, Revenue, Employee Satisfaction etc

d. What is Sharing
--------------------------------------------------------------------------------------------------------------------------
Sharing ideas and problem is the core of DEV-OPS, engages collaboration and the feedback loop.

--------------------------------------------------------------------------------------------------------------------------
Dev-OPS Principles:
--------------------------------------------------------------------------------------------------------------------------
Its often called - Three Ways Framework

a. Systems Thinking
--------------------------------------------------------------------------------------------------------------------------
Tells us to focus on the overall outcome of the pipeline. Its easy to think about optimize certain modules of pipeline, but that should not deteriorate the over all productivity of the pipeline.

For E.g.: Increasing the performance of application by vertical scaling in the pipeline, may very well move the bottlenecks to other modules in the pipeline.

b. Amplifying feedback loop
--------------------------------------------------------------------------------------------------------------------------
Creating / shortening the feedback loop between multiple teams in the organization. Short effective feedback loop is very important for development & operations, since its impact on the time to resolution. Always evaluate, how many more feedback loops can be built in your ecosystem.

c. Continuous Experimentation & Learning
--------------------------------------------------------------------------------------------------------------------------
Master new skills with repetition and work with a 'Fail-Fast' mindset.

--------------------------------------------------------------------------------------------------------------------------
Dev-OPS Practices:
--------------------------------------------------------------------------------------------------------------------------
1. Incident Command System: A good Incident command system that can work for both small and large incidents with consistency is useful

2. Developers on-Call: Sometimes it works, some it does not, since the person responding to the call, may not have actually developed the code or completely familiar with it.

3. Transparent Uptime: Whether you are running a public / private functionalities, communication is the key to maintain trust with next actions clearly called out in terms of service restoration

4. Blameless Postmortems : Their is no single root cause for a failure, and human error can happen. But to maintain a good culture, the teams should align with blameless postmortems.

5. Embedded Teams: Often the idea for a developer is to ship the code, and for operation is to deploy the code. Usually their is a gap in alignment in terms of 'When' to deploy the code and obviously 'its not my part' of the equation mindset. So if we have one operations engineer in every development team, it solves the problem, because that way you make the entire team responsible for the 'SUCCESS' and not either development or operations.

6. Cloud: Infrastructure as code has really enabled the way for operations team to adopt the cloud technologies. Enabling them with the ability to create / manage infrastructure components like any other code in the module with the help of multiple APIs.

7. Andon Cords: This was originally developed in a Toyota workshop, where its more like a stop request (like a string in a buss) to be called, if anybody identifies a problem, and stoping the propogation of that problem to later stages. In Software deployment its utilized to fail the deployment of a build if any one of the test cases are failing.

8. Dependency Injection: Its also called as 'Inversion of control', which focuses on loosely coupled dependency. In this pattern the application does not know anything about the dependencies, and they are passed to the application at run time. 

9. Blue-Green deployment: Traditional deployment are where you take down the software, upgrade to the newer version and then bring it back up and then continue doing it in the rolling fashion.
Their is another way of software deployment called the Blue-Green deployment, where their are two identical systems, one is online while the other is not and the traffic is managed by a load balancer. The new code is deployed to the offline site, tested and then traffic is sent to this system.
If there are any issues identified, you can shift back to the un-touched system and minimize the impact and the downtime.

10. Chaos Monkey: The idea behind this is to ensure developers dont rely on the infra-components to be always available and develop resiliency in the code itself.
Chaos Monkey, is a piece of software designed by Netflix, which would randomly go and trash their servers on the AWS cloud, so that the developers understand that not all components in their systems are always up and running and they build reliability into the software rather than relying on the components.

