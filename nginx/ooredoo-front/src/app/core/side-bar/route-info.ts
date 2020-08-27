// Sidebar route metadata
export interface RouteInfo {
  path: string;
  title: string;
  icon: string;
  class: string;
  label: string;
  labelClass: string;
  extralink: boolean;
  disabled: boolean;
  submenu: RouteInfo[];
}

export const ROUTES: RouteInfo[] = [
  {
    path: "/work-order/work-order-dashboard",
    title: "Automate",
    icon: "mdi mdi-gauge",
    class: "",
    label: "",
    labelClass: "",
    extralink: false,
    disabled: false,
    submenu: [],
  },
  {
    path: "/audit/dashboard",
    title: "Audit",
    icon: "mdi mdi-chart-bar",
    class: "",
    label: "",
    labelClass: "",
    extralink: false,
    disabled: false,
    submenu: [],
  },
  {
    path: "/collect/dashboard",
    title: "Collect",
    icon: "mdi mdi-collage",
    class: "",
    label: "",
    labelClass: "",
    extralink: false,
    disabled: false,
    submenu: [],
  },
  {
    path: "#",
    title: "Configuration",
    icon: "mdi mdi-settings",
    class: "",
    label: "",
    labelClass: "",
    extralink: false,
    disabled: false,
    submenu: [
      {
        path: "/devices/devices-dashboard",
        title: "Devices",
        icon: "",
        class: "",
        label: "",
        labelClass: "",
        extralink: false,
        disabled: false,
        submenu: [],
      },
    ],
  },
  {
    path: "#",
    title: "Manage Users",
    icon: "mdi mdi-account-circle",
    class: "",
    label: "",
    labelClass: "",
    extralink: false,
    disabled: false,
    submenu: [
      {
        path: "/users/users",
        title: "Users",
        icon: "",
        class: "",
        label: "",
        labelClass: "",
        extralink: false,
        disabled: false,
        submenu: [],
      },
      {
        path: "/roles/roles",
        title: "Roles",
        icon: "",
        class: "",
        label: "",
        labelClass: "",
        extralink: false,
        disabled: false,
        submenu: [],
      },
      {
        path: "/perm/perm",
        title: "Permissions",
        icon: "",
        class: "",
        label: "",
        labelClass: "",
        extralink: false,
        disabled: false,
        submenu: [],
      },
    ],
  },
];
