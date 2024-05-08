import kue from 'kue';
const concurrency = 2;
const queue = kue.createQueue({ concurrency });

const blacklisted = [4153518780, 4153518781];

const jobs = [
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

const sendNotification = (phoneNumber, message, job, done) => {
  const totalProgress = 100;
  let progressValue = 0; 
    
  const progressUpdateInterval = setInterval(() => {
    job.progress(progressValue, totalProgress);
    
    console.log(`Notification job ${job.id} ${progressValue}% complete`);
    
    if (progressValue >= totalProgress) {
      clearInterval(progressUpdateInterval);
      done();
    }
  }, 1000);
  if (blacklisted.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    progressValue = 50;
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
};

const pushNotificationQueue = queue;

jobs.forEach(jobData => {
  const job = pushNotificationQueue.create('push_notification_code_2', jobData).save(function(err) {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  pushNotificationQueue.on('job complete', function(id) {
    console.log(`Notification job ${id} completed`);
  });

  pushNotificationQueue.on('job failed', function(id) {
    console.log(`Notification job ${id} failed`);
  });

  sendNotification(jobData.phoneNumber, jobData.message, job, () => {});
});