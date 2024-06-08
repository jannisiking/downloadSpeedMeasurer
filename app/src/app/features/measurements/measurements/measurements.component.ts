import { Component, OnInit } from '@angular/core';
import {Observable, of} from "rxjs";
import {Measurement} from "../../../model/measurement";
import {BackendService} from "../../../services/backend.service";

@Component({
  selector: 'app-measurements',
  templateUrl: './measurements.component.html',
  styleUrls: ['./measurements.component.scss']
})
export class MeasurementsComponent implements OnInit {

  measurements$: Observable<Measurement[]> = of();

  constructor(
    private backendService: BackendService
  ) { }

  ngOnInit(): void {
    this.measurements$ = this.backendService.getMeasurements();
  }

}
