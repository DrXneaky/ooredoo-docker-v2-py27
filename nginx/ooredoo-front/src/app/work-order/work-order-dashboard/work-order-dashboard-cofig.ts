import { NavigationConfig } from 'src/app/shared/components/navigation-card/navigation-card-config';

export const WORKORDERMENU: NavigationConfig[] = [
    {
        title: 'B2B Services',
        icon: 'mdi mdi-account-circle text-info',
        description: 'generate workorder for different services(HSI, VPN, VoIP...)',
        path: '/work-order/work-order-b2b',
        disabled: false
    },
    {
        title: 'Advanced Services',
        icon: 'mdi mdi-weather-cloudy text-success',
        description: 'generate workorder for future customers!',
        path: '/work-order/work-order-advanced',
        disabled: false
    },
    {
        title: 'Mobile Services',
        icon: 'mdi mdi-radio-tower text-warning',
        description: 'description!',
        path: '/work-order/work-order-radio',
        disabled: false
    },
    {
        title: 'Trans Mngt Services',
        icon: 'mdi mdi-map-marker',
        description: 'generate workorder to supervise different microwave links',
        path: '/work-order/work-order-b2b',
        disabled: false
    }
];