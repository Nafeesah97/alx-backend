import kue from 'kue';
const queue = kue.createQueue();

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach(jobData => {
    const job = queue.create('push_notification_code_3', jobData).save(function(err) {
      if (!err) {
        console.log(`Notification job created: ${job.id}`)
      }
    });
    
    queue.on('job complete', function(id) {
      console.log(`Notification job ${id} completed`);
    });

    queue.on('job failed', function(id, err) {
      console.log(`Notification job ${id} failed: ${err}`);
    });

    queue.on('progress', function(progress) {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}