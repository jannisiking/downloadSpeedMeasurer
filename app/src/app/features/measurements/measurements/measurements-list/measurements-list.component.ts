import {Component, Input, OnInit} from '@angular/core';
import {Measurement} from "../../../../model/measurement";
import {Subject} from "rxjs";

@Component({
  selector: 'app-measurements-list',
  templateUrl: './measurements-list.component.html',
  styleUrls: ['./measurements-list.component.scss']
})
export class MeasurementsListComponent implements OnInit {

 @Input()
 set measurements(measurements: Measurement[]){
   this.measurements$.next(measurements);
 }

 measurements$ = new Subject<Measurement[]>();

  constructor() { }

  ngOnInit(): void {
  }

}
