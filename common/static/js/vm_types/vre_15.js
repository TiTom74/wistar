draw2d.shape.node.vre_15 = draw2d.shape.node.wistarSetParent.extend({
    NAME: "draw2d.shape.node.vre_15",
    VCPU: 1,
    VRAM: 512,
    ICON_WIDTH: 50,
    ICON_HEIGHT: 10,
    ICON_FILE: "/static/images/vre.png",

    INTERFACE_PREFIX: "ge-0/0/",
    INTERFACE_TYPE: "e1000",
    MANAGEMENT_INTERFACE_PREFIX: "fxp",
    MANAGEMENT_INTERFACE_INDEX: 0,
    MANAGEMENT_INTERFACE_TYPE: "e1000",
    DOMAIN_CONFIGURATION_FILE: "junos_vcp.xml",
    DUMMY_INTERFACE_LIST: ["2"],
    COMPANION_TYPE: "draw2d.shape.node.vriot",
    COMPANION_INTERFACE_LIST: ["1"],
    COMPANION_NAME_FILTER: "FPC|PFE|FP|pfe|fpc|fp|riot|RIOT",

    SECONDARY_DISK_PARAMS: {
        "type": "blank",
        "qemu_type": "qcow2",
        "size": "16G",
        "partition": true,
        "bus_type": "ide"
    },
    TERTIARY_DISK_PARAMS: {
        "type": "config_drive",
        "qemu_type": "raw",
        "bus_type": "ide"
    },
    CONFIG_DRIVE_SUPPORT: true,
    CONFIG_DRIVE_PARAMS: [
        {
            "template":  "vre_boot_loader.j2",
            "destination": "/boot/loader.conf"
        },
        {
            "template": "junos_config.j2",
            "destination": "/juniper.conf"
        }
    ]

});