# SDN-Based Real-Time Network Forensics and Anomaly Detection System

**Authors:** Kushal Kaparatti, Chinmay Paranjape, Chandsab Engineer, and Prathamesh Chitnis

---

## Abstract

The literature survey explores various aspects of Software-Defined Networking (SDN) and network forensics. It delves into SDN-based security mechanisms, forensic readiness, and attack detection methodologies. Topics include network visibility, forensic evidence collection, attack mitigation, and dynamic network management, with frameworks evaluated through simulations and real-world experiments. The survey identifies promising approaches and areas for future research.

---

## Key Studies

### Hyder et al. [1] - Crossfire DDoS Protection

A framework using Intent-Based Moving Target Defense (MTD) over SDN to protect against Crossfire Distributed Denial of Service (DDoS) attacks. The framework uses SDN’s programmability and ONOS Rest API with DNS port redirection for dynamic traffic management.

**Findings:** Effective in mitigating Crossfire DDoS attacks, with potential for scalability improvements.

### Chen et al. [2] - Cloud Forensics Framework

Proposed a digital forensics framework for detecting malicious behavior in cloud environments using SDN. It includes modules for full-traffic flow detection and memory analysis for identifying malicious behavior in virtual machines (VMs).

**Findings:** Effective in cloud-based environments like Baidu Cloud Storage, with future work suggested on enhancing semantic analysis.

### Ujcich et al. [3] - PROVINTENT Framework

A framework extension for SDN control plane tools that accounts for intent semantics, improving network visibility by recording the provenance of network intents.

**Findings:** Enables reasoning across abstractions but requires scalability improvements.

### Mugitama et al. [4] - OpenFlow-Based Forensics

A technical process for conducting SDN forensics using OpenFlow to capture and analyze network traffic, enhancing forensic accuracy.

**Findings:** Effective in real-world validation with potential scalability issues.

### Kim et al. [5] - BottleNet Framework

Designed to hide network bottlenecks from adversaries using SDN-based topology deception during link flooding attacks (LFAs).

**Findings:** Prevents the discovery of network bottlenecks through topology deception.

### Fernando [6] - Cyber Forensics Tools Review

A review on the effectiveness of cyber forensics tools, emphasizing the need for more advanced features due to the rapid evolution of technology.

**Findings:** Tools are effective but require enhancements to keep up with emerging challenges.

### Alsaedi et al. [7] - Flow-Based Reconnaissance Attack Detection

Utilizes OpenFlow features to detect flow-based reconnaissance attacks in SDN, leveraging flow entry counters and machine learning for classification.

**Findings:** Effective but needs improvements for scalability and integration.

### ÇİL et al. [8] - SDN Controllers Forensic Capabilities

A comparative analysis of SDN controllers’ forensic capabilities, highlighting strengths and weaknesses in handling forensic evidence.

**Findings:** Identified the need for better forensic features in SDN controllers.

### Waseem et al. [9] - SDN Forensics Future Technology

Explores future directions in SDN forensics, discussing the challenges and advantages of using SDN in forensic investigations.

**Findings:** Highlights SDN's role in improving forensic readiness.

### Ajiya et al. [10] - SDN Security Enhancements

Evaluates various security features in SDN environments, including intrusion detection and rule conflict resolution.

**Findings:** SDN provides enhanced security but introduces new challenges like DoS threats.

### Karie et al. [11] - Digital Forensic Readiness in SDN

Discusses the integration of Digital Forensic Readiness (DFR) in SDN environments, addressing the challenges posed by SDN’s centralized control architecture.

**Findings:** Proposes strategies like improved logging and real-time monitoring to enhance forensic readiness.

### Maulana et al. [12] - Network Attacks Classification

A literature review on using machine learning to classify network attacks for forensic investigations, focusing on algorithms like SVM.

**Findings:** Promising, but more work is needed to improve accuracy in real-world scenarios.

### Yurekten et al. [13] - SDN-Based Cyber Defense

A comprehensive survey on SDN-based defense mechanisms, creating a taxonomy of defense strategies for common attack types.

**Findings:** SDN is flexible and cost-efficient for cyber defense but requires better integration with existing infrastructure.

### Jiménez et al. [14] - Event Filtering Model for SDN Forensics

A model using artificial intelligence for event filtering in SDN-based digital forensics and incident response (DFIR).

**Findings:** Effective but needs scalability improvements.

### Wijayanto et al. [15] - ARP Spoofing Forensics

Proposed a framework using the TAARA method for network forensics against ARP spoofing attacks, involving systematic evidence collection and analysis.

**Findings:** Effective in mitigating ARP spoofing but needs better integration with existing systems.

---

## Conclusion

The survey highlights advancements in SDN-based security and forensic frameworks. Novel approaches like intent-based moving target defense and flow-based reconnaissance attack detection offer promising solutions. However, challenges remain in scalability, integration, and the need for enhanced forensic features in SDN controllers.

---

## References

1. M. F. Hyder and T. Fatima, “Towards crossfire distributed denial of service attack protection using intent-based moving target defense over software-defined networking,” IEEE Access, 2021.
2. G. Chen et al., “Research on digital forensics framework for malicious behavior in cloud,” IEEE, 2019.
3. B. E. Ujcich et al., “Provenance for intent-based networking,” IEEE, 2020.
4. S. A. Mugitama et al., “An evidence-based technical process for openflow-based sdn forensics,” IEEE, 2020.
5. J. Kim et al., “Bottlenet: Hiding network bottlenecks using sdn-based topology deception,” IEEE, 2021.
6. V. Fernando, “Cyber forensics tools: A review on mechanism and emerging challenges,” IFIP, 2021.
7. A. Alsaedi et al., “Flow-based reconnaissance attacks detection in sdn-based environment,” 2022.
8. A. ÇİL, “A comparative analysis of software-defined network controllers in terms of network forensics processes and capabilities,” Sigma, 2024.
9. Q. Waseem et al., “Future technology: Software-defined network (sdn) forensic,” Symmetry, 2021.
10. A. Ajiya et al., “A review on software defined network (sdn) based network security enhancements,” 2021.
11. N. Karie et al., “Digital forensic readiness implementation in sdn,” 2021.
12. M. Maulana et al., “Network attacks classification for network forensics investigation: Literature reviews,” Jurnal RESTI, 2023.
13. O. Yurekten et al., “Sdn-based cyber defense: A survey,” Future Generation Computer Systems, 2021.
14. M. B. Jiménez et al., “A filtering model for evidence gathering in an sdn-oriented digital forensic and incident response context,” IEEE Access, 2024.
15. A. Wijayanto et al., “Network forensics against address resolution protocol spoofing attacks using trigger, acquire, analysis, report, action method,” Register Jurnal Ilmiah, 2022.