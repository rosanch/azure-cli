# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PipelineRunResponse(Model):
    """The response properties returned for a pipeline run.

    :param status: The current status of the pipeline run.
    :type status: str
    :param imported_artifacts: The artifacts imported in the pipeline run.
    :type imported_artifacts: list[str]
    :param progress: The current progress of the copy operation.
    :type progress: ~containerregistry.models.ProgressProperties
    :param start_time: The time the pipeline run started.
    :type start_time: datetime
    :param finish_time: The time the pipeline run finished.
    :type finish_time: datetime
    :param source: The source of the pipeline run.
    :type source: ~containerregistry.models.ImportPipelineSourceProperties
    :param target: The target of the pipeline run.
    :type target: ~containerregistry.models.ExportPipelineTargetProperties
    :param catalog_digest: The digest of the tar used to transfer the
     artifacts.
    :type catalog_digest: str
    :param trigger: The trigger that caused the pipeline run.
    :type trigger: ~containerregistry.models.PipelineTriggerDescriptor
    :param pipeline_run_error_message: The detailed error message for the
     pipeline run in the case of failure.
    :type pipeline_run_error_message: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'imported_artifacts': {'key': 'importedArtifacts', 'type': '[str]'},
        'progress': {'key': 'progress', 'type': 'ProgressProperties'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'source': {'key': 'source', 'type': 'ImportPipelineSourceProperties'},
        'target': {'key': 'target', 'type': 'ExportPipelineTargetProperties'},
        'catalog_digest': {'key': 'catalogDigest', 'type': 'str'},
        'trigger': {'key': 'trigger', 'type': 'PipelineTriggerDescriptor'},
        'pipeline_run_error_message': {'key': 'pipelineRunErrorMessage', 'type': 'str'},
    }

    def __init__(self, *, status: str=None, imported_artifacts=None, progress=None, start_time=None, finish_time=None, source=None, target=None, catalog_digest: str=None, trigger=None, pipeline_run_error_message: str=None, **kwargs) -> None:
        super(PipelineRunResponse, self).__init__(**kwargs)
        self.status = status
        self.imported_artifacts = imported_artifacts
        self.progress = progress
        self.start_time = start_time
        self.finish_time = finish_time
        self.source = source
        self.target = target
        self.catalog_digest = catalog_digest
        self.trigger = trigger
        self.pipeline_run_error_message = pipeline_run_error_message
