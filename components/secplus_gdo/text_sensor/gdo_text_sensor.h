#pragma once

#include "esphome/components/text_sensor/text_sensor.h"

namespace esphome {
namespace secplus_gdo {

class GDOTextSensor : public text_sensor::TextSensor {
 public:
  GDOTextSensor() = default;

  void set_sync_state(bool synced) { this->publish_state(synced ? "Synced" : "Not Synced"); }
  void set_component_source(const std::string &source) { this->component_source_ = source; }
  void set_type(uint8_t type) { this->type_ = type; }
  uint8_t get_type() const { return this->type_; }

 protected:
  uint8_t type_;
  std::string component_source_;
};

}  // namespace secplus_gdo
}  // namespace esphome
