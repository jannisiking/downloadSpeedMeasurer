import {Component, OnInit} from '@angular/core';
import {BackendService} from "./services/backend.service";
import {Observable, of} from "rxjs";
import {Measurement} from "./model/measurement";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'app';

  measurements$: Observable<Measurement[]> = of();

  constructor(private backendService: BackendService) {
  }

  ngOnInit() {
    this.measurements$ = this.backendService.getMeasurements();
  }


}
