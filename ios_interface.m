#import "ViewController.h"

// 1. Подключаем библиотеки
#import "ESTConfig.h"
#import "EILIndoorLocationManager.h"
#import "EILRequestFetchLocation.h"
#import "EILOrientedPoint.h"

// 2. Добавляем протокол EILIndoorLocationManagerDelegate

@interface ViewController () <EILIndoorLocationManagerDelegate>

// 3. Добавляем свойство определения местоположения

@property (nonatomic) EILIndoorLocationManager *locationManager;
@end
@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // 4. Иллюстрирование объекта местоположения и установка его делегирования
    self.locationManager = [EILIndoorLocationManager new];
    self.locationManager.delegate = self;
}

// Подключаем функцию выгрузки карты с аккаунта Estimote

[ESTConfig setupAppID:@"<App ID>" andAppToken:@"<App Token>"];

// Добавляем свойство выгрузки метаданных в класс ViewController

@property (nonatomic) EILIndoorLocationManager *locationManager;
@property (nonatomic) EILLocation *location;

// Внизу функции viewDidLoad добавляем оставшуюся часть кода для обнаружения локации

EILRequestFetchLocation *fetchLocationRequest =
      [[EILRequestFetchLocation alloc] initWithLocationIdentifier:@"railway-mos"];
[fetchLocationRequest sendRequestWithCompletion:^(EILLocation *location,
                                                    NSError *error) {

  if (location != nil) {
    self.location = location;
  } else {
    NSLog(@"can't fetch location: %@", error);
  }
}];

// Теперь, когда данные о локации безопасно хранятся, подключаем функцию непрерывного обновления позиционирования

self.location = location;
[self.locationManager startPositionUpdatesForLocation:self.location];

// Добавляем методы передачи обновления позиционирования 

-(void)indoorLocationManager:(EILIndoorLocationManager *)manager
didFailToUpdatePositionWithError:(NSError *)error {
    NSLog(@"failed to update position: %@", error);
}

-(void)indoorLocationManager:(EILIndoorLocationManager *)manager
          didUpdatePosition:(EILOrientedPoint *)position
            withAccuracy:(EILPositionAccuracy)positionAccuracy
              inLocation:(EILLocation *)location {
    NSString *accuracy;
    switch (positionAccuracy) {
        case EILPositionAccuracyVeryHigh: accuracy = @"+/- 1.00m"; break;
        case EILPositionAccuracyHigh: accuracy = @"+/- 1.62m"; break;
        case EILPositionAccuracyMedium: accuracy = @"+/- 2.62m"; break;
        case EILPositionAccuracyLow: accuracy = @"+/- 4.24m"; break;
        case EILPositionAccuracyVeryLow: accuracy = @"+/- ? :-("; break;
        case EILPositionAccuracyUnknown: accuracy = @"unknown"; break;
    }
    NSLog(@"x: %5.2f, y: %5.2f, orientation: %3.0f, accuracy: %@",
          position.x, position.y, position.orientation, accuracy);
}
