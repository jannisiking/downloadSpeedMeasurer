import {AfterContentInit, Component, Input, OnDestroy, OnInit} from '@angular/core';
import {Measurement} from "../../../../model/measurement";
import {Subject, takeUntil} from "rxjs";
import {Chart, ChartItem} from "chart.js";

@Component({
  selector: 'app-measurements-graph',
  templateUrl: './measurements-graph.component.html',
  styleUrls: ['./measurements-graph.component.scss']
})
export class MeasurementsGraphComponent implements OnInit, OnDestroy, AfterContentInit {

  @Input()
  set measurements(measurements: Measurement[]) {
    this.measurements$.next(measurements);
  }

  destroy$ = new Subject<void>();

  measurements$ = new Subject<Measurement[]>()

  ctx: HTMLCanvasElement = {} as any;

  constructor() {
  }

  ngOnInit(): void {}

  ngOnDestroy() {
    this.destroy$.next();
  }

  ngAfterContentInit() {
    this.ctx = document.getElementById('myChart') as HTMLCanvasElement;

    this.measurements$
      .pipe(
        takeUntil(this.destroy$)
      )
      .subscribe(measurements => {
        if (this.ctx !== null) {
          new Chart(this.ctx, {
            type: 'line',
            data: {
              labels: measurements.map(measurement => measurement.time.toString()),
              datasets: [
                {
                  label: 'Durschnittl. mb/s',
                  data: measurements.map(measurement => measurement.avg_mbps),
                  borderColor: 'rgb(75, 192, 192)',
                  tension: 0.1
                }
              ]

            },
          });
        }
      })

  }

}
