import {Component, Input, OnInit} from '@angular/core';
import {Measurement} from "../../../../model/measurement";
import {Subject} from "rxjs";

@Component({
  selector: 'app-measurements-graph',
  templateUrl: './measurements-graph.component.html',
  styleUrls: ['./measurements-graph.component.scss']
})
export class MeasurementsGraphComponent implements OnInit {

  @Input()
  set measurements(measurements: Measurement[]){
    this.measurements$.next(measurements);
  }

  measurements$ = new Subject<Measurement[]>()

  constructor() { }

  ngOnInit(): void {
  }

}
