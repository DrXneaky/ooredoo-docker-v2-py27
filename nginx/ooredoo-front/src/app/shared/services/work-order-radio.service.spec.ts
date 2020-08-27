import { TestBed } from '@angular/core/testing';

import { WorkOrderRadioService } from './work-order-radio.service';

describe('WorkOrderRadioService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: WorkOrderRadioService = TestBed.get(WorkOrderRadioService);
    expect(service).toBeTruthy();
  });
});
