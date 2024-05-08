import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
  phoneNumber: string,
  message: string,
};

const job = queue.create('push_notification_code', jobData).save(function(err) {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

queue.on('job complete', function(id) {
  console.log('Notification job completed');
});

queue.on('job failed', function(id) {
  console.log('Notification job failed');
});