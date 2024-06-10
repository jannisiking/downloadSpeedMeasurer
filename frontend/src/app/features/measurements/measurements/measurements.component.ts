import {Component, OnInit} from '@angular/core';
import {Observable, of} from "rxjs";
import {Measurement} from "../../../model/measurement";
import {BackendService} from "../../../services/backend.service";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-measurements',
  templateUrl: './measurements.component.html',
  styleUrls: ['./measurements.component.scss']
})
export class MeasurementsComponent implements OnInit {

  measurements$: Observable<Measurement[]> = of();

  dateForm: FormGroup;

  constructor(
    private backendService: BackendService,
    private formBuilder: FormBuilder
  ) {
    this.dateForm = this.formBuilder.group({
      startDate: [null, Validators.required],
      endDate: [null, Validators.required],
    });
  }

  ngOnInit(): void {
    this.refreshMeasurements();
  }

  onSubmit(){
    this.refreshMeasurements();
  }

  refreshMeasurements(){
    this.measurements$ = this.backendService.getMeasurements(
      this.dateForm.get('startDate')?.value,
      this.dateForm.get('endDate')?.value)
  }

}
