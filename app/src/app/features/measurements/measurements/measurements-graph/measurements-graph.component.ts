import {AfterContentInit, Component, Input, OnDestroy, OnInit} from '@angular/core';
import {Measurement} from "../../../../model/measurement";
import {Subject, takeUntil} from "rxjs";
import {Chart, registerables} from "chart.js";

@Component({
  selector: 'app-measurements-graph',
  templateUrl: './measurements-graph.component.html',
  styleUrls: ['./measurements-graph.component.scss']
})
export class MeasurementsGraphComponent implements OnInit, OnDestroy {

  @Input()
  set measurements(measurements: Measurement[]) {
    this.measurements$.next(measurements);
  }

  destroy$ = new Subject<void>();

  measurements$ = new Subject<Measurement[]>()

  chart: any = [];

  constructor() {
    Chart.register(...registerables)
  }

  ngOnInit(): void {

    this.measurements$
      .pipe(
        takeUntil(this.destroy$)
      )
      .subscribe(measurements => {
        const datasets = [
          {
            label: 'Durschnittl. mb/s',
            data: measurements.map(measurement => measurement.avg_mbps),
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
          }
        ]

        const labels = measurements.map(measurement => measurement.timestamp.toString());

        new Chart('canvas', {
          type: 'line',
          data: {
            labels: labels,
            datasets: datasets
          },
        });
      })

  }

  ngOnDestroy() {
    this.destroy$.next();
  }

}
