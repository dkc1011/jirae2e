def bpmnName = "new_bpmn"

pipeline {
   agent any

    triggers {
      gitlab(
        triggerOnPush: true,
        triggerOnMergeRequest: true
    }

   stages {
      stage('Cloning Git') {
        steps {
            git 'https://github.com/jimmyrabbit88/jirae2e'
        }
      }

      stage('run'){
          steps {
              sh 'python3 ./JIRA-E2E.py'
          }
      }

      stage('features'){
          steps {
              sh """
              git clone https://github.com/jimmyrabbit88/features.git
              mv ${bpmnName}.feature features
              cd features
              git add .
              git commit -m "msg"
              git remote set-url origin https://jimmyrabbit88:safehouse30011988@github.com/jimmyrabbit88/features
              git push origin master
              """
          }
      }


   }

   post {
    always {
      cleanWs deleteDirs: true
    }
  }


}