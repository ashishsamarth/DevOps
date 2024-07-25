**Jenkins-Installation**
--------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------------------------------
1. Install Java
Java-11 is out of support, so preference is Java-17 or Java-21

    dnf install java-17-openjdf -y

2. Validate the Java-version by eecuting the following command on the terminal

    java --version

    ![Github Images](/Jenkins/Assets/Jenkins-Install-Java-17.JPG)

3. If for some reason, java --version is not showing up the correct java version, check if you have multiple versions installed and then select the required version

    update-alternatives --config java

    ![Github Images](/Jenkins/Assets/jenkins-select-java-version.JPG)

4. If for some reason, the above approach still does not work, perform the following

    a. cd /etc/profile.d
    b. whereis java
        It will provide you multiple locations, out of that list go for
        ls -lrt /usr/bin/java : This should point you to /etc/alternatives/java , which is a symbolic link for the actual location of java

    ![Github Images](/Jenkins/Assets/Jenkins-whereis-java.JPG)
        
    c. create a new file java.sh and export the following variables to it
        export JAVA_HOME=<*Path to the actual location of java*>
        export PATH=$PATH:$JAVA_HOME/bin
    
    d. source the java.sh file for the variables to take effect

        source /etc/profile.d/java.sh
    
    e. validate the newly updated java version. if required, update the path of the symbolic to the actual path of $JAVA_HOME/bin/java

        cd /etc/alternatives
        ln -sfn <*Path to the actual location of java directory/bin/java*> java

    ![Github Images](/Jenkins/Assets/Jenkins-Symbolic-Link-Java.JPG)

5. 