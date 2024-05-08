import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue({ disableSearch: true, jobEvents: false, redis: { db: 3 } });
    kue.Job.rangeByType('push_notification_code_3', 'inactive', 0, -1, 'asc', (err, jobs) => {
      jobs.forEach(job => job.remove());
    });
  });

  afterEach(() => {
    queue.testMode.exit();
  });

  it('create two new jobs to the queue', async () => {
    const list = [
      { phoneNumber: '1234567890', message: 'Test message 1' },
      { phoneNumber: '9876543210', message: 'Test message 2' }
    ];
  
    await createPushNotificationsJobs(list, queue);
  
    expect(queue.testMode.jobs.length).to.equal(2);
  
    expect(queue.testMode.jobs[0].data).to.deep.equal(list[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(list[1]);
  });
});
