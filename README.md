## bdd_framework


## 生成种子数据

    sh scripts/seed_data.sh

## 清除数据
    
    sh scripts/clean_db.sh
    
## 数据库迁移
 
### 首次运行

    python migrate.py db init
    
运行这个命令后会在项目目录中添加 migrations 目录。

创建第一个版本：

    python migrate.py db migrate -m "initial migration"

运行迁移：

    python migrate.py db upgrade

### 后续迁移

更新models目录下的文件

运行：

    python migrate.py db migrate -m "migrate message"
    python migrate.py db upgrade


## appium

    export ANDROID_HOME="/Users/ethan.zhang/Library/Android/sdk"
    export PATH=$ANDROID_HOME/platform-tools:$PATH
    export PATH=$ANDROID_HOME/tools:$PATH
    export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk-9.0.4.jdk/Contents/Home"
    export PATH=$JAVA_HOME/bin:$PATH



