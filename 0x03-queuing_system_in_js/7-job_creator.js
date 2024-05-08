import kue from 'kue';
const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const sendNotification = (job, done) => {
  const totalProgress = 100;
  let progressValue = 0; 
  
  const progressUpdateInterval = setInterval(() => {
    progressValue += 1;
  
    job.progress(progressValue, totalProgress);
  
    console.log(`Notification job ${job.id} ${progressValue}% complete`);
  
    if (progressValue >= totalProgress) {
      clearInterval(progressUpdateInterval);
      done();
    }
  }, 1000);
};
  
queue.on('job complete', function(id) {
    console.log('Notification job completed');
  });
      
queue.on('job failed', function(id) {
  console.log('Notification job failed');
});

jobs.forEach(jobData => {
  const job = queue.create('push_notification_code', jobData).save(function(err) {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  sendNotification(job, () => {});
});